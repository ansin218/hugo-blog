---
title: "Mode of a Column in Python R Sql"
date: 2019-03-26T13:03:15+01:00
draft: true
---

Given a table or dataframe named <strong>students: </strong>

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

## Mode of a column in SQL:

```SQL
-- MySQL
SELECT Degree_Length
FROM Degree 
GROUP BY Degree_Length 
ORDER BY COUNT(*) DESC
LIMIT 1

-- Oracle
SELECT Degree_Length
FROM
   (SELECT Degree_Length, COUNT(1) 
      FROM Degree
      GROUP BY Degree_Length
      ORDER BY COUNT(1) DESC) temp
WHERE rownum = 1
```

## Mode of a column in Python:

```Python
degree['degree_length'].mode()
```

## Mode of a column in R:

```C
# Using tail, names, sort and table
tail(names(sort(table(degree$degree_length))), 1)

# Using names, sort and table
names(sort(-table(degree$degree_length)))[1]

# Using unique, tabulate and max
uniqueVal <- unique(degree$degree_length)
tabulatedVal <- tabulate(match(degree$degree_length, uniqueVal))
uniqueVal[tabulatedVal == max(tabulatedVal)]
```

<strong>Output:</strong>

```C
4
```