---
title: "Median of a Column in Python R Sql"
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

## Median of a column in SQL:

```SQL
-- For MySQL
SET @rowindex := -1;
 
SELECT AVG(d2.Degree_Length) as Median
FROM
   (SELECT @rowindex:=@rowindex + 1 AS rowindex,
           d1.Degree_Length AS Degree_Length
    FROM Degree d1
    ORDER BY d1.Degree_Length) AS d2
WHERE d2.rowindex IN (FLOOR(@rowindex / 2) , CEIL(@rowindex / 2));

-- For Oracle
SELECT Degree_Country, MEDIAN(Degree_Length)
FROM Degree
GROUP BY Degree_Country;
```

## Median of a column in Python:

```Python
degree['degree_length'].median()
```

## Median of a column in R:

```C
median(degree$degree_length, na.rm = TRUE)
```

<strong>Output:</strong>

```C
3
```