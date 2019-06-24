---
title: "Get all records in SQL, Python and R"
date: 2019-06-01T14:53:25+01:00
description: "Get all records from a table in SQL or get all records from a dataframe using pandas in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe.

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
SELECT * FROM students
```

## Select all rows using Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

students
```

## Select all rows using R:

```Java
students
```

## Result:

```Java
   student_id student_name student_city student_country
0           1         John      Atlanta             USA
1           2         Hari       Mumbai           India
2           3          Ali        Dubai             UAE
3           4        Jenny       Berlin         Germany
4           5         Lisa       Berlin         Germany
5           6        Priya        Delhi           India
6           7         Wong      Beijing           China
7           8       Julius         Rome           Italy
8           9       Alonso      Atlanta             USA
9          10         Noor       London              UK
```