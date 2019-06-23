---
title: "Mode per Group in Python R Sql"
date: 2019-04-17T19:48:25+02:00
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

## Mode per group in SQL:

```SQL
-- MySQL
WITH FreqOccurence AS
     (SELECT p.degree_country, p.degree_length, COUNT(*) AS occurence
        FROM degree AS p
       GROUP BY p.degree_country, p.degree_length
     )
SELECT s.degree_country, s.degree_length
  FROM FreqOccurence AS s
  JOIN (SELECT s.degree_country, MAX(s.occurence) AS max_occurence
          FROM FreqOccurence AS s
         GROUP BY s.degree_country
       ) AS m
    ON s.degree_country = m.degree_country AND s.occurence = m.max_occurence

-- Oracle
select degree_country, degree_length
from   (select degree_country, degree_length, count(*) cnt, max(count(*)) over (partition by degree_country) max_count
from   degree
group by degree_country, degree_length)
where  cnt = max_count
```

## Mode per group in Python:

```Python
degree.groupby(['degree_country'])['degree_length'].agg(pd.Series.mode).reset_index()
```

## Mode per group in R:

```C
degree %>% group_by(degree_country) %>% count(degree_length) %>% top_n(1)
```

<strong>Output:</strong>

```Java
  degree_country degree_length
0      Australia             1
1          China             3
2        Germany        [3, 4]
3          India             4
4    Switzerland             4
5             UK             4
6            USA             3
```