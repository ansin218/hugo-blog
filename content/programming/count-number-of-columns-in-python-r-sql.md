---
title: "Count Number Of Columns In R, Python And SQL"
date: 2019-03-12T14:53:25+01:00
draft: true
---

Given a table or dataframe named <strong>students: </strong>

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
| 6          | Priya        | Delhi        | Mumbai          |
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

## Count number of rows of table in SQL:

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

## Count number of columns of dataframe in Python:

```Python
# Method 1 using len
len(students.columns)

# Method 2 using shape
students.shape[1]
```

## Count number of columns of dataframe in R:

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