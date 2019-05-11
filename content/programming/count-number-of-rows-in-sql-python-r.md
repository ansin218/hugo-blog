---
title: "Count number of rows in SQL, Python and R"
date: 2019-05-02T14:53:25+01:00
description: "Count the number of rows in a table using SQL or the number of rows in a dataframe using Pandas in Python or R."
image: "https://images2.imgbox.com/01/52/a3D7Ccw7_o.jpg"
draft: true
---

Given a table or dataframe named *__students__* as shown below, count the number of rows in the given table or dataframe.

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

## Count number of rows in a table using SQL:

```SQL
SELECT count(*) FROM students
```

## Count number of rows in a dataframe using Python:

```Python
import pandas as pd

# Method 1 using len
len(students)

# Method 2 using shape
students.shape[0]

# Method 3 using count
students['student_id'].count()
```

## Count number of rows in a dataframe using R:

```C
# Method 1 using nrow
nrow(students)

# Method 2 using dim
dim(students)[1]
```

<strong>Output:</strong>

```C
10
```