---
title: "Filtering rows using AND in SQL, Python and R"
date: 2019-05-01T10:03:06+02:00
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
SELECT * 
FROM students
WHERE student_country = 'India'
AND student_city = 'Mumbai'
```

## Filtering rows in Python:

```Python
# Method 1 using only '&'
students[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 2 using loc and '&'
students.loc[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 3 using query and 'and'
students.query('student_country == "India" and student_city == "Mumbai"')
```

## Filtering rows in R:

```C
# Method 1 using only '&'
students[students$student_country == "India" & students$student_city == "Mumbai",]

# Method 2 using which
students[which(students$student_country == "India" & students$student_city == "Mumbai"),]

# Method 3 using dplyr
filter(students, student_country == "India" & student_city == "Mumbai")

# Method 4 using subset
subset(students, student_country == "India" & student_city == "Mumbai")
```

<strong>Output:</strong>

```C
   student_id student_name student_city student_country
1           2         Hari       Mumbai           India
```