---
title: "Filtering rows using BETWEEN operator in SQL, Python and R"
date: 2019-05-07T15:10:43+02:00
description: "Filter all the rows using BETWEEN operator from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__degree__* as shown below, get all the records from the table or dataframe where the length of pursuing the degree is between 1 and 3 years.

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

## Filtering rows using BETWEEN operator in SQL:

```SQL
SELECT * 
FROM degree
WHERE degree_length BETWEEN 1 AND 3
```

## Filtering rows using BETWEEN operator in Python:

```Python
degree[degree['degree_length'].between(1, 3)]
```

## Filtering rows using BETWEEN operator in R:

```C
# Method 1 using only filter
degree %>% filter(degree_length %in% (1:3))

# Method 2 using subset
subset(degree, degree_length %in% (1:3))

# Method 3 using between
degree %>% filter(between(degree_length, 1, 3))
```

## Result: 

```C
    degree_id  student_id degree_name degree_country  degree_length
0           1           1     B. Arts            USA              3
2           3           2          MS            USA              2
6           7           4      M. Sc.        Germany              3
7           8           7          BS          China              3
8           9           7          MS      Australia              1
9          10           7         PhD            USA              3
12         13           6          ME          India              2
```