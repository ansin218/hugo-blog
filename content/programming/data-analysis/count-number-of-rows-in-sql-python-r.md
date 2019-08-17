---
title: "Count number of rows in SQL, Python and R"
date: 2019-06-01T14:54:25+01:00
description: "Count the number of rows in a table using SQL or the number of rows in a dataframe using Pandas in Python or R."
image: "https://images2.imgbox.com/1e/2e/wepOioBd_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, count the number of rows in the given table or dataframe.

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

## Count number of rows in a table using SQL:

```SQL
SELECT count(*) FROM students
```

## Count number of rows in a dataframe using Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
len(students)

# Method 2
students.shape[0]

# Method 3
students['student_id'].count()
```

## Count number of rows in a dataframe using R:

```C
# Method 1
nrow(students)

# Method 2
dim(students)[1]
```

### Result:

```C
10
```