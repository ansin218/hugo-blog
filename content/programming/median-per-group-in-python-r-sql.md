---
title: "Median per Group in Python R Sql"
date: 2019-03-26T13:28:57+01:00
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

## Median per group in SQL:

```SQL
SELECT Degree_Country, AVG(Degree_Length)
FROM Degree
GROUP BY Degree_Country;
```

## Median per group in Python:

```Python
# Using agg
degree.groupby('degree_country')['degree_length'].agg('median')

# Using apply and numpy
degree.groupby(['degree_country'])[['degree_length']].apply(np.nanmedian)
```

## Median per group in R:

```C
# Using aggregate
aggregate(degree$degree_length, list(degree$degree_country), median)

# Using ddply
ddply(degree, .(degree_country), summarize,  Mean_Col = median(degree_length))

# Using group_by and summarise_at
degree %>% group_by(degree_country) %>% summarise_at(vars(degree_length), median)

# Using setDT and lapply
setDT(degree)[, lapply(.SD, median), by=.(degree_country), .SDcols = c("degree_length")]
```

<strong>Output:</strong>

```C
   degree_country degree_length
1:            USA           3.0
2:          India           4.0
3:        Germany           3.5
4:    Switzerland           4.0
5:          China           3.0
6:      Australia           1.0
7:             UK           4.0
```