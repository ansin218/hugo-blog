---
title: "Count number of columns in SQL, Python and R"
date: 2019-05-03T14:53:25+01:00
description: "Count the number of columns in a table using SQL or the number of columns in a dataframe using Pandas in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, count the number of columns in the given table or dataframe.

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

## Count number of columns in a table using SQL:

```SQL
-- For MySQL
SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'students'

-- For Oracle
SELECT count(*)
FROM user_tab_columns
WHERE table_name = 'STUDENTS'
```

## number of columns in a dataframe in Python:

```Python
# Method 1 using len
len(students.columns)

# Method 2 using shape
students.shape[1]
```

## number of columns in a dataframe in R:

```C
# Method 1 using ncol
ncol(students)

# Method 2 using dim
dim(students)[2]
```

<strong>Output:</strong>

```C
4
```