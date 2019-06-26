---
title: "Filtering rows using regular expression in SQL, Python and R"
date: 2019-05-07T15:10:43+02:00
description: "Filter all the rows using regular expression (regex) from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the country the student comes from contains the character *__"y"__* or *__"d"__* using regular expression.

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

## Filtering rows using regular expreesion in SQL:

```SQL
-- For MySQL
SELECT * 
FROM students
WHERE student_country REGEXP '[y|d]'

-- For Oracle
SELECT * 
FROM students
WHERE  REGEXP_LIKE (student_country, '(y|d)');
```

## Filtering rows using regular expreesion in Python:

```Python
students[students['student_country'].str.contains(r'y|d',regex=True)]
```

## Filtering rows using regular expreesion in R:

```Java
# Method 1 using only grep
students[grep('(y|d)', students$student_country),]

# Method 2 using dplyr and stringr
students %>% filter(str_detect(student_country, '(y|d)'))
```

## Result:

```Java
  student_id student_name student_city student_country
1          2         Hari       Mumbai           India
2          4        Jenny       Berlin         Germany
3          5         Lisa       Berlin         Germany
4          6        Priya        Delhi           India
5          8       Julius         Rome           Italy
```