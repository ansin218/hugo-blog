---
title: "Filtering rows using NOT operator in SQL, Python and R"
date: 2019-05-07T16:03:06+02:00
description: "Filter all the rows using NOT operation from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the student hails from anywhere but India.

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

## Filtering rows using NOT operator in SQL:

```SQL
SELECT * 
FROM students
WHERE student_country = 'India'
```

## Filtering rows using AND operator in Python:

```Python
# Method 1 using only '&'
students[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 2 using loc and '&'
students.loc[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 3 using query and 'and'
students.query('student_country == "India" and student_city == "Mumbai"')
```

## Filtering rows using AND operator in R:

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