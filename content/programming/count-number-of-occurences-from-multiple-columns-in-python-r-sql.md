---
title: "Count Number of Occurences From Multiple Columns in Python R Sql"
date: 2019-03-22T14:14:16+01:00
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

## Count value occurence from multiple columns in SQL:

```SQL
SELECT Student_Country, Student_City, Count(*)
FROM Students
GROUP BY Student_Country, Student_City
```

## Count value occurence from multiple columns in Python:

```Python
# Using groupby and size
students.groupby(['student_city', 'student_country']).size()
```

## Count value occurence from multiple columns in R:

```C
# Using count
count(students, c('student_country', 'student_city'))

# Using aggregate
aggregate(numeric(nrow(students)), students[c('student_country', 'student_city')], length) 

# Using ddply
ddply(students, .(student_country, student_city), nrow)
```

<strong>Output:</strong>

```C
  student_country student_city V1
            China      Beijing  1
          Germany       Berlin  2
            India        Delhi  1
            India       Mumbai  1
            Italy         Rome  1
              UAE        Dubai  1
               UK       London  1
              USA      Atlanta  2
```