---
title: "Unique Values of Column in Python R Sql"
date: 2019-03-21T14:37:12+01:00
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

## Get unique values of column in SQL:

```SQL
SELECT DISTINCT(Student_Country) FROM Students
```

## Get unique values of column in Python:

```Python
# Using unique
students['student_country'].unique()

# Using drop_duplicates
students.drop_duplicates('student_country')['student_country']
```

## Get unique values of column in R:

```C
# Using unique
unique(students$student_country)

# Using levels
levels(students$student_country)

# Using distinct
distinct(students, student_country)
```

<strong>Output:</strong>

```C
['USA', 'India', 'UAE', 'Germany', 'China', 'Italy', 'UK']
```
