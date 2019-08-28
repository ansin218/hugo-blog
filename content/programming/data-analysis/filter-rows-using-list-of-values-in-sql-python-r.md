---
title: "Filtering rows using list of values in SQL, Python and R"
date: 2019-06-02T15:03:06+02:00
description: "Filter all the rows using list of values from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/69/70/oOtPwVKm_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the student hails from India or Italy.

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

## Filtering rows using list of values in SQL:

```SQL
SELECT * 
FROM students
WHERE student_country IN ('India', 'Italy')
```

## Filtering rows using list of values in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
students[students.student_country.isin(['India', 'Italy'])]

# Method 2
students.loc[students.student_country.isin(['India', 'Italy'])]
```

## Filtering rows using list of values in R:

{{% notice warning %}}
You must have the *__[dplyr](https://dplyr.tidyverse.org/)__* library installed to run method 4.
{{% /notice %}}

```C
# Method 1
students[students$student_country %in% c('India', 'Italy'), ]

# Method 2
subset(students, students$student_country %in% c('India', 'Italy'))

# Method 3
students[which(students$student_country %in% c('India', 'Italy')), ]

# Method 4
library('dplyr')

filter(students, students$student_country %in% c('India', 'Italy'))
```

### Result: 

```C
student_id student_name student_city student_country
          2         Hari       Mumbai           India
          6        Priya        Delhi           India
          8       Julius         Rome           Italy
```