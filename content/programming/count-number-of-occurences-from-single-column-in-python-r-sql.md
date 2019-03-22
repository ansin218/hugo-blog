---
title: "Count Number of Occurences From Single Column in Python R Sql"
date: 2019-03-22T14:14:05+01:00
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

## Count value occurence from a single column in SQL:

```SQL
SELECT Student_Country, Count(*)
FROM Students
GROUP BY Student_Country
```

## Count value occurence from a single column in Python:

```Python
# Using value_counts
students['student_country'].value_counts()

# Using groupby and size
students.groupby(['student_country']).size()

# Using groupby and lambda
students[['student_country']].apply(lambda x: x.value_counts())
```

## Count value occurence from a single column in R:

```C
# Using count
count(students, "student_country")

# Using aggregate
aggregate(numeric(nrow(students)), students[c("student_country")], length) 

# Using ddply
ddply(students, .(student_country), nrow)
```

<strong>Output:</strong>

```C
  student_country V1
            China  1
          Germany  2
            India  2
            Italy  1
              UAE  1
               UK  1
              USA  2
```