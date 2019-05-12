---
title: "Filtering Rows Using or in Python R Sql"
date: 2019-05-09T15:10:43+02:00
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

## Filtering rows in SQL:

```SQL
-- For MySQL
SELECT * 
FROM students
WHERE student_country LIKE '%in%' COLLATE utf8_bin

-- For Oracle
SELECT * 
FROM students
WHERE student_country LIKE '%in%'
```

## Filtering rows in Python:

```Python
# Method 1 using contains
students[students['student_country'].str.contains('in')]

# Method 2 using query and contains
students.query('student_country.str.contains("in")', engine='python')
```

## Filtering rows in R:

```C
# Method 1 using grep
students[grep("in", students$student_country), ]

# Method 2 using str_detect
filter(students, str_detect(student_country, "in"))
```

<strong>Output:</strong>

```C
  student_id student_name student_city student_country
1          7         Wong      Beijing           China
```