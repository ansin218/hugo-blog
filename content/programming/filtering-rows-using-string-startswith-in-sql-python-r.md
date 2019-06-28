---
title: "Filter Rows Using String Startswith in Sql Python R"
date: 2019-05-30T11:13:12+02:00
draft: true
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the country the student comes from contains *__in__* taking case sensitivity into account.

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

## Filtering rows using case sensitive string in SQL:

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

## Filtering rows using case sensitive string in Python:

```Python
import pandas as pd

# Method 1
students.loc[students['student_country'].str.startswith('I')]

# Method 2
students[students['student_country'].str.startswith('I')]

# Method 3
students.query('student_country.str.startswith("I")', engine = 'python')
```

## Filtering rows using case sensitive string in R:

```Java
# Method 1
students[startsWith(as.character(students$student_country), 'I'),]

# Method 2
require("data.table")

students[grepl('^I', students$student_country), ]

# Method 3
students[students$student_country %like% "^I", ]
```

## Reults:

```Java
  student_id student_name student_city student_country
2          2         Hari       Mumbai           India
6          6        Priya        Delhi           India
8          8       Julius         Rome           Italy
```