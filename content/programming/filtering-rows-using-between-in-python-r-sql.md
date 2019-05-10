---
title: "Filtering Rows Using or in Python R Sql"
date: 2019-05-09T15:10:43+02:00
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

## Filtering rows in SQL:

```SQL
SELECT * 
FROM degree
WHERE degree_length BETWEEN 1 AND 3
```

## Filtering rows in Python:

```Python
degree[degree['degree_length'].between(1, 3)]
```

## Filtering rows in R:

```C
# Method 1 using only filter
degree %>% filter(degree_length %in% (1:3))

# Method 2 using subset
subset(degree, degree_length %in% (1:3))

# Method 3 using between
degree %>% filter(between(degree_length, 1, 3))
```

<strong>Output:</strong>

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