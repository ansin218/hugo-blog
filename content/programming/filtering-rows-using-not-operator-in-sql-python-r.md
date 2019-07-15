---
title: "Filtering rows using NOT operator in SQL, Python and R"
date: 2019-06-02T16:03:06+02:00
description: "Filter all the rows using NOT operation from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/e9/7c/BSVPEwZH_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the student hails from anywhere but India.

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

## Filtering rows using NOT operator in SQL:

```SQL
-- Method 1
SELECT * 
FROM students
WHERE student_country != 'India'

-- Method 2
SELECT * 
FROM students
WHERE student_country <> 'India'
```

## Filtering rows using NOT operator in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
students.loc[students.student_country != 'India']

# Method 2
students.loc[~(students.student_country == 'India')]

# Method 3
students.query('student_country != "India"')
```

## Filtering rows using NOT operator in R:

{{% notice warning %}}
You must have the *__[dplyr](https://dplyr.tidyverse.org/)__* library installed to run method 7 and 8.
{{% /notice %}}

```C
# Method 1
students[!(students$student_country == "India"),]

# Method 2
students[students$student_country != "India",]

# Method 3
students[which(!students$student_country == "India"),]

# Method 4
students[which(students$student_country != "India"),]

# Method 5
subset(students, student_country != "India")

# Method 6
subset(students, !student_country == "India")

# Method 7
filter(students, student_country != "India")

# Method 8
filter(students, !(student_country == "India"))
```

## Result:

```C
   student_id student_name student_city student_country
1           1         John      Atlanta             USA
3           3          Ali        Dubai             UAE
4           4        Jenny       Berlin         Germany
5           5         Lisa       Berlin         Germany
7           7         Wong      Beijing           China
8           8       Julius         Rome           Italy
9           9       Alonso      Atlanta             USA
10         10         Noor       London              UK
```