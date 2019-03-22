---
title: "Count Unique Values of Multiple Columns in Python R Sql"
date: 2019-03-22T11:14:42+01:00
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
SELECT COUNT(DISTINCT(Student_Country)), COUNT(DISTINCT(Student_City)) FROM Students
```

## Count unique values of a single column in Python:

```Python
# Using nunique
students.nunique()

# Using drop_duplicates and len
students.describe(include='all').loc['unique', :]
```

## Count unique values of a single column in R:

```C
# Using unique and rapply
rapply(students,function(x)length(unique(x)))

# Using summarise_all and n_distinct
students %>% summarise_all(funs(n_distinct(.)))
```

<strong>Output:</strong>

```C
student_city student_country
           8               7
```