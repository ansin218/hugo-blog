---
title: "Filtering rows using regular expression in SQL, Python and R"
date: 2019-06-02T16:10:43+02:00
description: "Filter all the rows using regular expression (regex) from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/a6/70/pCqMFfFL_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the country the student comes from contains the character *__"y"__* or *__"d"__* using regular expression.

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

## Filtering rows using regular expreesion in SQL:

```SQL
-- For MySQL
SELECT * 
FROM students
WHERE student_country REGEXP '[y|d]'

-- For Oracle
SELECT * 
FROM students
WHERE  REGEXP_LIKE (student_country, '(y|d)');
```

## Filtering rows using regular expreesion in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

students[students['student_country'].str.contains(r'y|d',regex=True)]
```

## Filtering rows using regular expreesion in R:

{{% notice warning %}}
You must have the *__[dplyr](https://www.rdocumentation.org/packages/dplyr/versions/0.7.8)__* and *__[stringr](https://www.rdocumentation.org/packages/stringr/versions/1.4.0)__* libraries installed to run method 2.
{{% /notice %}}

```Java
# Method 1
students[grep('(y|d)', students$student_country),]

# Method 2
students %>% filter(str_detect(student_country, '(y|d)'))
```

## Result:

{{% notice info %}}
The following output has been taken directly from a Python, SQL or R console using one of the methods demonstrated above. Hence, the way the result is displayed may not look exactly like the one below for all cases always.
{{% /notice %}}

```C
  student_id student_name student_city student_country
1          2         Hari       Mumbai           India
2          4        Jenny       Berlin         Germany
3          5         Lisa       Berlin         Germany
4          6        Priya        Delhi           India
5          8       Julius         Rome           Italy
```