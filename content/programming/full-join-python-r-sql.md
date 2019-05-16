---
title: "Full Join Python R Sql"
date: 2019-04-17T19:49:06+02:00
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

```
| ----------------- | ---------- | ------- | -------------- | ------------- |
| Student_Degree_ID | Student_ID | Degree  | Degree_Country | Degree_Length |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 1                 | 1          | B. Arts | USA            | 3             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 2                 | 2          | B. Tech | India          | 4             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 3                 | 2          | MS      | USA            | 2             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 4                 | 2          | PhD     | USA            | 5             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 5                 | 3          | B. Sc.  | Germany        | 4             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 6                 | 4          | B. Sc.  | Switzerland    | 4             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 7                 | 4          | M. Sc.  | Germany        | 3             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 8                 | 7          | BS      | China          | 3             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 9                 | 7          | MS      | Australia      | 1             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 10                | 7          | PhD     | USA            | 3             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 11                | 10         | BE      | UK             | 4             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 12                | 6          | BE      | India          | 4             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 13                | 6          | ME      | India          | 2             |
| ----------------- | ---------- | ------- | -------------- | ------------- |
```

## Full Join in SQL:

```SQL
-- For MySQL
SELECT s.student_id, s.student_name, d.degree, d.degree_length FROM students s
LEFT JOIN degree d ON s.student_id = d.student_id  
UNION
SELECT s.student_id, s.student_name, d.degree, d.degree_length FROM students s
RIGHT JOIN degree d ON s.student_id = d.student_id 

-- For Oracle
SELECT s.student_id, s.student_name, d.degree, d.degree_country
FROM students s
FULL JOIN degree d
ON s.student_id = d.student_id
```

## Full join in Python:

```Python
pd.merge(students, degree, on = ['student_id'], how = 'outer')[['student_id', 'student_name', 'degree_name']]
```

## Full join in R:

```C
merge(x = students, y = degree, by = "student_id", all = TRUE)[, c("student_id", "student_name", "degree_name")]
```

<strong>Output:</strong>

```C
    student_id student_name degree_name
 1:          1         John     B. Arts
 2:          2         Hari     B. Tech
 3:          2         Hari          MS
 4:          2         Hari         PhD
 5:          3          Ali      B. Sc.
 6:          4        Jenny      B. Sc.
 7:          4        Jenny      M. Sc.
 8:          5         Lisa          NA
 9:          6        Priya          BE
10:          6        Priya          ME
11:          7         Wong          BS
12:          7         Wong          MS
13:          7         Wong         PhD
14:          8       Julius          NA
15:          9       Alonso          NA
16:         10         Noor          BE
```