---
title: "Mean per Group in Python R Sql"
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

## Mean per group in SQL:

```SQL
SELECT Degree_Country, AVG(Degree_Length)
FROM Degree
GROUP BY Degree_Country;
```

## Mean per group in Python:

```Python
degree.groupby('degree_country')['degree_length'].agg('mean')
```

## Mean per group in R:

```C
# Using aggregate
aggregate(degree$degree_length, list(degree$degree_country), mean)

# Using ddply
ddply(degree, .(degree_country), summarize,  Mean_Col = mean(degree_length))

# Using group_by and summarise_at
degree %>% group_by(degree_country) %>% summarise_at(vars(degree_length), mean)

# Using setDT and lapply
setDT(degree)[, lapply(.SD, mean), by=.(degree_country), .SDcols = c("degree_length")]
```

<strong>Output:</strong>

```C
   degree_country degree_length
1:            USA      3.250000
2:          India      3.333333
3:        Germany      3.500000
4:    Switzerland      4.000000
5:          China      3.000000
6:      Australia      1.000000
7:             UK      4.000000
```