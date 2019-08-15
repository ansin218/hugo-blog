---
title: "Unique Values of Multiple Columns In Python, R and SQL"
date: 2019-03-22T13:16:27+01:00
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

## Get unique values of multiple columns in SQL:

```SQL
SELECT DISTINCT Student_City, Student_Country
FROM Students
```

## Get unique values of multiple columns in Python:

```Python
# Using drop_duplicates
students.drop_duplicates(['student_city', 'student_country'])[['student_city', 'student_country']]

# Using factorize
pd.factorize(list(zip(students['student_city'], students['student_country'])))

# Using groupby and size
students.groupby(['student_city', 'student_country']).size()
```

## Get unique values of multiple columns in R:

```C
# Using unique
unique(students[c('student_city', 'student_country')])

# Using distinct
students %>% distinct(student_city, student_country)

# Using aggregate
aggregate(numeric(nrow(students)), students[c("student_city", "student_country")], length) 
```

<strong>Output:</strong>

```C
  student_city student_country
       Atlanta             USA
        Mumbai           India
         Dubai             UAE
        Berlin         Germany
         Delhi           India
       Beijing           China
          Rome           Italy
        London              UK
```
