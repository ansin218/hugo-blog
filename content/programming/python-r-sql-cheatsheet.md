---
title: "Cheatsheet for SQL, Python and R"
date: 2019-05-01T10:38:17+02:00
draft: true
---

<table>
  <tr>
    <td><b>Method</b></td>
    <td><b>SQL</b></td>
    <td><b>Python</b></td>
    <td><b>R</b></td>
  </tr>

  <!-- Get all records -->
  <tr>
    <td><h4><a href = "/programming/get-all-records-in-sql-python-r/">Get all records</a></h4></td>
    <td><pre>SELECT * FROM table<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
  </tr>

  <!-- Count number of rows -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-rows-in-sql-python-r/">Count number of rows</a></h4></td>
    <td><pre>
SELECT count(*)
FROM students<span class = "copy-to-clipboard"></pre></td>
    <td><pre>
# Method 1 using len
len(students)

# Method 2 using shape
students.shape[0]

# Method 3 using count
students['student_id'].count()
    <span class = "copy-to-clipboard"></pre></td>
    <td><pre>
# Method 1 using nrow
nrow(students)

# Method 2 using dim
dim(students)[1]    
    <span class = "copy-to-clipboard"></pre></td>
  </tr>

  <!-- Count number of columns -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-columns-in-sql-python-r/">Count number of columns</a></h4></td>
    <td><pre>
-- For MySQL
SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'students'

-- For Oracle
SELECT count(*)
FROM user_tab_columns
WHERE table_name = 'STUDENTS'    
    <span class = "copy-to-clipboard"></pre></td>
    <td><pre>
# Using len
len(students.columns)

# Using shape
students.shape[1]
    <span class = "copy-to-clipboard"></pre></td>
    <td><pre>
# Using ncol
ncol(students)

# Using dim
dim(students)[2]   
    <span class = "copy-to-clipboard"></pre></td>
  </tr>
</table>

The End.