---
title: "Filtering rows using string starting with specific pattern in SQL, Python and R"
date: 2019-06-10T11:13:19+02:00
description: "Filter all the rows using string starting with a specific pattern from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/a6/70/pCqMFfFL_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the country the student comes from starts with *__I__*.

```
| ---------- | ------------ | ------------ | --------------- |
| student_id | student_name | student_city | student_country |
| ---------- | ------------ | ------------ | --------------- |
| 1          | John         | Atlanta      | USA             |
| ---------- | ------------ | ------------ | --------------- |
| 2          | Hari         | Mumbai       | India           |
| ---------- | ------------ | ------------ | --------------- |
| 3          | Ali          | Dubai        | UAE             |
| ---------- | ------------ | ------------ | --------------- |
| 4          | Jenny        | Berlin       | Germany         |
| ---------- | ------------ | ------------ | --------------- |
| 5          | Lisa         | Berlin       | Germany         |
| ---------- | ------------ | ------------ | --------------- |
| 6          | Priya        | Delhi        | India           |
| ---------- | ------------ | ------------ | --------------- |
| 7          | Wong         | Beijing      | China           |
| ---------- | ------------ | ------------ | --------------- |
| 8          | Julius       | Rome         | Italy           |
| ---------- | ------------ | ------------ | --------------- |
| 9          | Alonso       | Atlanta      | USA             |
| ---------- | ------------ | ------------ | --------------- |
| 10         | Noor         | London       | UK              |
| ---------- | ------------ | ------------ | --------------- |
```

## Filtering rows using string starting with specific pattern in SQL:

```SQL
-- For MySQL
SELECT * 
FROM students
WHERE student_country LIKE 'I%' COLLATE utf8_bin

-- For Oracle
SELECT * 
FROM students
WHERE student_country LIKE 'I%'
```

## Filtering rows using string starting with specific pattern in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
students.loc[students['student_country'].str.startswith('I')]

# Method 2
students[students['student_country'].str.startswith('I')]

# Method 3
students.query('student_country.str.startswith("I")', engine = 'python')
```

## Filtering rows using string starting with specific pattern in R:

{{% notice warning %}}
You must have the *__[data.table](https://github.com/Rdatatable/data.table/wiki)__* library installed to run method 4.
{{% /notice %}}

```C
# Method 1
students[startsWith(as.character(students$student_country), 'I'),]

# Method 2
students[students$student_country %like% "^I", ]

# Method 3
require("data.table")

students[grepl('^I', students$student_country), ]
```

## Reults:

```C
student_id student_name student_city student_country
         2         Hari       Mumbai           India
         6        Priya        Delhi           India
         8       Julius         Rome           Italy
```