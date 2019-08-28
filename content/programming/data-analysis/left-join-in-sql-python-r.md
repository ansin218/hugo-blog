---
title: "Left join in SQL, Python and R"
date: 2019-05-05T19:48:45+02:00
description: "Left join of two tables or dataframes using SQL, Python and R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given two tables or dataframes named *__students__* and *__degree__* as shown below, perform a left join operation on the following tables using *__student_id__* and return records having columns *__student_id__*, *__student_name__* and *__degree_name__*.

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

## Left join in SQL:

```SQL
SELECT s.student_id, s.student_name, d.degree, d.degree_country
FROM students s
LEFT JOIN degree d
ON s.student_id = d.student_id
```

## Left join in Python:

```Python
pd.merge(students, degree, on = ['student_id'], how = 'left')[['student_id', 'student_name', 'degree_name']]
```

## Left join in R:

```C
merge(x = students, y = degree, by = "student_id", all.x = TRUE)[, c("student_id", "student_name", "degree_name")]
```

<strong>Output:</strong>

```C
   student_id student_name degree_name
1           1         John     B. Arts
2           2         Hari     B. Tech
3           2         Hari          MS
4           2         Hari         PhD
5           3          Ali      B. Sc.
6           4        Jenny      B. Sc.
7           4        Jenny      M. Sc.
8           5         Lisa        <NA>
9           6        Priya          BE
10          6        Priya          ME
11          7         Wong         PhD
12          7         Wong          BS
13          7         Wong          MS
14          8       Julius        <NA>
15          9       Alonso        <NA>
16         10         Noor          BE
```