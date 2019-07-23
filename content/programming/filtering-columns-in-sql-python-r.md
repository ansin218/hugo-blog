---
title: "Display specific columns in SQL, Python and R"
date: 2019-06-07T15:03:06+02:00
description: "Display specific columns from the given table in SQL or given dataframe in Pandas using Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe but show only the names of the student and the city they come from.

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

## Filter and subset columns in SQL:

```SQL
SELECT student_name, student_country
FROM students
```

## Filter and subset columns in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

students[['student_name', 'student_city']]
```

## Filter and subset columns in R:

```C
students[, c('student_name', 'student_city')]
```

## Result:

```C
student_name student_city
        John      Atlanta
        Hari       Mumbai
         Ali        Dubai
       Jenny       Berlin
        Lisa       Berlin
       Priya        Delhi
        Wong      Beijing
      Julius         Rome
      Alonso      Atlanta
        Noor       London
```