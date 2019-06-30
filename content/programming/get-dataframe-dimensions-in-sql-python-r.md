---
title: "Get dataframe dimensions in SQL, Python and R"
date: 2019-06-01T14:57:25+01:00
description: "Get dimensions of the dataframe or table using SQL, Python or R. Dimensions return the number of rows and columns in the given table or dataframe."
image: "https://images2.imgbox.com/e9/7c/BSVPEwZH_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get the dimensions of the given table or dataframe. In other words, get the number of rows and columns in the given table or dataframe.

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

## Get dimensions of table in SQL:

```SQL
-- For MySQL
SELECT SUM(t1.TABLE_ROWS)/COUNT(t1.TABLE_ROWS) AS ROWS, COUNT(*) AS COLUMNS
FROM information_schema.TABLES AS t1
LEFT JOIN information_schema.COLUMNS t2  
ON t1.TABLE_NAME = t2.TABLE_NAME 
WHERE t1.TABLE_NAME = 'students'
GROUP BY t2.TABLE_NAME;

-- For Oracle
SELECT t.num_rows AS ROWS, Count(*) AS COLUMNS
FROM all_tables t
LEFT JOIN all_tab_columns c
ON t.table_name = c.table_name
WHERE num_rows IS NOT NULL AND t.table_name = 'STUDENTS'
GROUP BY t.num_rows
```

## Get dimensions of dataframe in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
students.shape

# Method 2
students.info()
```

## Get dimensions of dataframe in R:

```C
dim(students)
```

### Result:

{{% notice info %}}
The following output has been taken directly from a Python, SQL or R console using one of the methods demonstrated above. Hence, the way the result is displayed may not look exactly like the one below for all cases always.
{{% /notice %}}

```C
Rows Columns
  10       4
```