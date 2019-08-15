---
title: "Left join without intersection in SQL, Python and R"
date: 2019-05-06T14:20:16+02:00
description: "Left join without intersection of two tables or dataframes using SQL, Python and R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given two tables or dataframes named *__students__* and *__degree__* as shown below, perform a left join without intersection operation on the following tables using *__student_id__* and return all the records from the table on the left (*__students__*) excluding the common ones matching with the table on the right (*__degree__*). They must be having the following columns: *__student_id__*, and *__student_name__*. In other words, perform an anti-join operation as shown in the picture.

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

```
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| student_degree_id | student_id | degree_name  | degree_country | degree_length |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 1                 | 1          | B. Arts      | USA            | 3             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 2                 | 2          | B. Tech      | India          | 4             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 3                 | 2          | MS           | USA            | 2             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 4                 | 2          | PhD          | USA            | 5             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 5                 | 3          | B. Sc.       | Germany        | 4             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 6                 | 4          | B. Sc.       | Switzerland    | 4             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 7                 | 4          | M. Sc.       | Germany        | 3             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 8                 | 7          | BS           | China          | 3             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 9                 | 7          | MS           | Australia      | 1             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 10                | 7          | PhD          | USA            | 3             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 11                | 10         | BE           | UK             | 4             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 12                | 6          | BE           | India          | 4             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
| 13                | 6          | ME           | India          | 2             |
| ----------------- | ---------- | ------------ | -------------- | ------------- |
```

## Left join without intersection in SQL:

```SQL
SELECT s.student_id, s.student_name
FROM students s
LEFT JOIN degree d
ON s.student_id = d.student_id
WHERE d.student_id IS NULL
```

## Left join without intersection in Python:

```Python
# Method 1 using isin
students[~students['student_id'].isin(degree['student_id'])][['student_id', 'student_name']]

# Method 2 using merge
students.merge(degree, indicator = True, how = 'left')[lambda x: x._merge == 'left_only'].drop('_merge', 1)[['student_id', 'student_name']]
```

## Left join without intersection in R:

```C
# Method 1 using dplyr
anti_join(students, degree, by = 'student_id')[, c("student_id", "student_name")]

# Method 2 using data.table
setDT(students)[!degree, on="student_id"][, c("student_id", "student_name")]

# Method 3 using in clause
students[!students$student_id %in% degree$student_id,][, c("student_id", "student_name")]
```

<strong>Output:</strong>

```
  student_id student_name
1          8       Julius
2          9       Alonso
3          5         Lisa
```