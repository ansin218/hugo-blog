---
title: "Sum of a column in SQL, Python and R"
date: 2019-06-06T13:03:15+01:00
description: "Calculate the sum of a column from a given table in SQL. Calculate the sum of column from a dataframe using Python or R."
image: "https://images2.imgbox.com/1e/be/QVjZXuJG_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, calculate the total duration taken by all the students across all their degrees. In other words, calculate the total number of years spent using the column, *__degree_length__*.

```
| ----------------- | ---------- | ------- | -------------- | ------------- |
| student_degree_id | student_id | degree  | degree_country | degree_length |
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

## Sum of a column in SQL:

```SQL
SELECT SUM(degree_length)
FROM degree
```

## Sum of a column in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

degree['degree_length'].sum()
```

## Sum of a column in R:

```C
sum(degree$degree_length, na.rm = TRUE)
```

### Result:

```C
42
```