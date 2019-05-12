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

  <!-- GET ALL RECORDS -->
  <tr>
    <td><h4><a href = "/programming/get-all-records-in-sql-python-r/">Get all records</a></h4></td>
    <td><pre><code class="language-SQL">SELECT * FROM table</code></pre></td>
    <td><pre><code class="language-Python">dataframe</code></pre></td>
    <td><pre><code class="language-C">dataframe</code></pre></td>
  </tr>

  <!-- COUNT NUMBER OF ROWS -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-rows-in-sql-python-r/">Count number of rows</a></h4></td>
    <td><pre><code class="language-SQL">SELECT count(*)
FROM table
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using len
len(df)

# Method 2 using shape
df.shape[0]

# Method 3 using count
df['id'].count()
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using nrow
nrow(df)

# Method 2 using dim
dim(df)[1]
</code></pre></td>
  </tr>

  <!-- COUNT NUMBER OF COLUMNS -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-columns-in-sql-python-r/">Count number of columns</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'students'

-- For Oracle
SELECT count(*)
FROM user_tab_columns
WHERE table_name = 'STUDENTS'
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using len
len(students.columns)

# Method 2 using shape
students.shape[1]
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using ncol
ncol(students)

# Method 2 using dim
dim(students)[2]
</code></pre></td>
  </tr>

  <!-- GET DATAFRAME DIMENSIONS -->
  <tr>
    <td><h4><a href = "/programming/get-dataframe-dimensions-in-sql-python-r/">Get dataframe dimensions</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT SUM(t1.TABLE_ROWS)/COUNT(t1.TABLE_ROWS) AS ROWS, COUNT(*) AS COLUMNS
FROM information_schema.TABLES AS t1
LEFT JOIN information_schema.COLUMNS t2  
ON t1.TABLE_NAME = t2.TABLE_NAME 
WHERE t1.TABLE_NAME = 'students'
GROUP BY t2.TABLE_NAME;

-- For Oracle
SELECT t.num_rows AS ROWS, Count(*) AS COLUMNS
FROM all_tables t
LEFT JOIN all_tab_columns c
ON t.table_name = c.table_name
WHERE num_rows IS NOT NULL 
AND t.table_name = 'STUDENTS'
GROUP BY t.num_rows
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using shape
students.shape

# Method 2 using info
students.info()
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using dim
dim(students)
</code></pre></td>
  </tr>
</table>

The End.