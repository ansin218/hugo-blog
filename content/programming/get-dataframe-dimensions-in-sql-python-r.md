---
title: "Get Dataframe Dimensions In SQL, Python and R"
date: 2019-05-01T14:57:25+01:00
description: "Get dimensions of the dataframe or table using SQL, Python or R. Dimensions return the number of rows and columns in the table or dataframe."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, get the dimensions of the given table or dataframe. In other words, get the number of rows and columns in the given table or dataframe.

```
| ---------- | ------------ | ------------ | --------------- |
| Student_ID | Student_Name | Student_City | Student_Country |
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

```Python
# Method 1 using shape
students.shape

# Method 2 using info
students.info()
```

## Get dimensions of dataframe in R:

```C
# Method 1 using dim
dim(students)
```

<strong>Output:</strong>

```C
(10, 4)
```