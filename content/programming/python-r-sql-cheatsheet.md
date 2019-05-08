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
  <tr>
    <td><h4><a href = "/programming/get-all-records-in-sql-python-r/">Get All Records</a></h4></td>
    <td><pre>SELECT * FROM table<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
  </tr>
  <tr>
    <td><h4><a href = "/programming/count-number-of-rows-in-sql-python-r/">Count All Rows</a></h4></td>
    <td><pre>SELECT count(*) FROM students<span class = "copy-to-clipboard"></pre></td>
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
</table>


The End.


| Left align | Right align | Center align |
|:-----------|------------:|:------------:|
| This       |        This |     This     |
| column     |      column |    column    |
| will       |        will |     will     |
| be         |          be |      be      |
| left       |       right |    center    |
| aligned    |     aligned |    aligned   |

asdasd