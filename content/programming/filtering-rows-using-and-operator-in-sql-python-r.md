---
title: "Filtering rows using AND operator in SQL, Python and R"
date: 2019-06-02T10:03:06+02:00
description: "Filter all the rows using AND operation from the given table in SQL or given dataframe in Python or R."
image: "https://images2.imgbox.com/1e/be/QVjZXuJG_o.jpg"
---

Given a table or dataframe named *__students__* as shown below, get all the records from the table or dataframe where the student hails from India and specifically, comes from Mumbai.

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

## Filtering rows using AND operator in SQL:

```SQL
SELECT * 
FROM students
WHERE student_country = 'India'
AND student_city = 'Mumbai'
```

## Filtering rows using AND operator in Python:

{{% notice warning %}}
You must have the *__[pandas](https://pandas.pydata.org/)__* library installed to run this snippet of code.
{{% /notice %}}

```Python
import pandas as pd

# Method 1
students[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 2
students.loc[(students.student_country == 'India') & (students.student_city == 'Mumbai')]

# Method 3
students.query('student_country == "India" and student_city == "Mumbai"')
```

## Filtering rows using AND operator in R:

```C
# Method 1
students[students$student_country == "India" & students$student_city == "Mumbai",]

# Method 2
students[which(students$student_country == "India" & students$student_city == "Mumbai"),]

# Method 3
filter(students, student_country == "India" & student_city == "Mumbai")

# Method 4
subset(students, student_country == "India" & student_city == "Mumbai")
```

## Result:

{{% notice info %}}
The following output has been taken directly from a Python, SQL or R console using one of the methods demonstrated above. Hence, the way the result is displayed may not look exactly like the one below for all cases always.
{{% /notice %}}

```C
   student_id student_name student_city student_country
1           2         Hari       Mumbai           India
```