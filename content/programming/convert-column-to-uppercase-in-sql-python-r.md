---
title: "Convert column to uppercase in SQL, Python and R"
date: 2019-06-07T15:03:06+02:00
description: "Convert specific column from the given table in SQL or given dataframe in Python or R to uppercase."
image: "https://images2.imgbox.com/69/70/oOtPwVKm_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, convert all the names of the students to uppercase.

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
SELECT UPPER(student_name)
FROM students
```

## Filtering rows using list of values in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

students['student_name'].str.upper()
```

## Filtering rows using list of values in R:

```C
toupper(students$student_name)
```

### Result:

```C
      JOHN
      HARI
       ALI
     JENNY
      LISA
     PRIYA
      WONG
    JULIUS
    ALONSO
      NOOR
```