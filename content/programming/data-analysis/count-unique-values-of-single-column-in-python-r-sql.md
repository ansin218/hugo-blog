---
title: "Count Unique Values Of A Single Column In Python, R And SQL"
date: 2019-03-21T16:56:59+01:00
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

## Count unique values of a single column in SQL:

```SQL
SELECT COUNT(DISTINCT(Student_Country)) FROM Students
```

## Count unique values of a single column in Python:

```Python
# Using nunique
students['student_country'].nunique()

# Using drop_duplicates and len
len(students.drop_duplicates('student_country')['student_country'])
```

## Count unique values of a single column in R:

```C
# Using unique and length
length(unique(students$student_country))

# Using levels and length
length(levels(students$student_country))
```

<strong>Output:</strong>

```C
7
```