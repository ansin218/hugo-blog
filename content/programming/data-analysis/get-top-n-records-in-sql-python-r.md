---
title: "Get top N records in SQL, Python and R"
date: 2019-06-10T14:53:25+01:00
description: "Get top N records from a table in SQL or from a dataframe using pandas in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below,  get first 5 records from the given table using SQL or the given dataframe using Python or R.

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

## Select all rows using SQL:

```SQL
-- MySQL
SELECT * 
FROM students  
LIMIT 5

-- Oracle
SELECT * 
FROM students  
FETCH NEXT 5 ROWS ONLY
```

## Select all rows using Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

students.head(5)
```

## Select all rows using R:

```C
head(students, 5)
```

## Result:

```C
student_id student_name student_city student_country
         1         John      Atlanta             USA
         2         Hari       Mumbai           India
         3          Ali        Dubai             UAE
         4        Jenny       Berlin         Germany
         5         Lisa       Berlin         Germany
```