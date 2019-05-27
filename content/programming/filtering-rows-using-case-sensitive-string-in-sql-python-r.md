---
title: "Filtering Rows Using or in Python R Sql"
date: 2019-05-07T15:10:43+02:00
description: "Filter all the rows using case sensitive string from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
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
# Method 1 using contains and lower
students[students['student_country'].str.lower().str.contains('in')]

# Method 2 using contains and case parameter
students[students['student_country'].str.contains('in', case = False)]

# Method 3 using query and contains
students.query('student_country.str.lower().str.contains("in")', engine = 'python')
```

## Filtering rows in R:

```C
# Method 1 using grep and tolower
students[grep("in", tolower(students$student_country)), ]

# Method using grep and ignore.case
students[grep("in", students$student_country, ignore.case=TRUE), ]

# Method 3 using str_detect
filter(students, str_detect(tolower(student_country), "in"))
```

<strong>Output:</strong>

```C
   student_id student_name student_city student_country
1           2         Hari       Mumbai           India
5           6        Priya        Delhi           India
6           7         Wong      Beijing           China
```