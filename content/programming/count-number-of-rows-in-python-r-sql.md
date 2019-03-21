---
title: "Count Number Of Rows In R, Python And SQL"
date: 2019-03-12T14:53:25+01:00
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
| 6          | Priya        | Delhi        | Mumbai          |
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

## Count number of rows of table in SQL:

```SQL
SELECT count(*) FROM students
```

## Count number of rows of dataframe in Python:

```Python
# Method 1 using len
len(students)

# Method 2 using shape
students.shape[0]

# Method 3 using count
students['Student_ID'].count()
```

## Count number of rows of dataframe in R:

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