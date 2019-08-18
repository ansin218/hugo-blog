---
title: "Cheatsheet for SQL, Python and R"
date: 2019-05-21T10:38:17+02:00
description: "Cheatsheet for basic data analysis commands using SQL, Python and R."
image: "https://images2.imgbox.com/fc/ff/gYk0Dxly_o.jpg"
draft: true
---

<table name = "cheatsheet" id = "cheatsheet">
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
    <td><pre><code class="language-Java">dataframe</code></pre></td>
  </tr>

  <!-- COUNT NUMBER OF ROWS -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-rows-in-sql-python-r/">Count number of rows</a></h4></td>
    <td><pre><code class="language-SQL">SELECT count(*)
FROM table
</code></pre></td>
    <td><pre><code class="language-Python">len(df)</code></pre></td>
    <td><pre><code class="language-Java">nrow(df)</code></pre></td>
  </tr>

  <!-- COUNT NUMBER OF COLUMNS -->
  <tr>
    <td><h4><a href = "/programming/count-number-of-columns-in-sql-python-r/">Count number of columns</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'TABLE_NAME'

-- For Oracle
SELECT count(*)
FROM user_tab_columns
WHERE table_name = 'TABLE_NAME'
</code></pre></td>
    <td><pre><code class="language-Python">len(df.columns)</code></pre></td>
    <td><pre><code class="language-Java">ncol(df)</code></pre></td>
  </tr>

  <!-- GET DATAFRAME DIMENSIONS -->
  <tr>
    <td><h4><a href = "/programming/get-dataframe-dimensions-in-sql-python-r/">Get dataframe dimensions</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT SUM(t1.TABLE_ROWS)/COUNT(t1.TABLE_ROWS) AS ROWS, COUNT(*) AS COLUMNS
FROM information_schema.TABLES AS t1
LEFT JOIN information_schema.COLUMNS t2  
ON t1.TABLE_NAME = t2.TABLE_NAME 
WHERE t1.TABLE_NAME = 'TABLE_NAME'
GROUP BY t2.TABLE_NAME;

-- For Oracle
SELECT t.num_rows AS ROWS, Count(*) AS COLUMNS
FROM all_tables t
LEFT JOIN all_tab_columns c
ON t.table_name = c.table_name
WHERE num_rows IS NOT NULL 
AND t.table_name = 'TABLE_NAME'
GROUP BY t.num_rows
</code></pre></td>
    <td><pre><code class="language-Python">df.shape</code></pre></td>
    <td><pre><code class="language-Java">dim(df)
</code></pre></td>
  </tr>

  <!-- FILTERING USING AND -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-and-operator-in-sql-python-r/">Filtering using AND operator</a></h4></td>
    <td><pre><code class="language-SQL">SELECT * 
FROM students
WHERE student_country = 'India'
AND student_city = 'Mumbai'
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using only '&amp;'
students[(students.student_country == 'India') &amp; (students.student_city == 'Mumbai')]

# Method 2 using loc and '&amp;'
students.loc[(students.student_country == 'India') &amp; (students.student_city == 'Mumbai')]

# Method 3 using query and 'and'
students.query('student_country == &quot;India&quot; and student_city == &quot;Mumbai&quot;')
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using only '&amp;'
students[students$student_country == &quot;India&quot; &amp; students$student_city == &quot;Mumbai&quot;,]

# Method 2 using which
students[which(students$student_country == &quot;India&quot; &amp; students$student_city == &quot;Mumbai&quot;),]

# Method 3 using dplyr
filter(students, student_country == &quot;India&quot; &amp; student_city == &quot;Mumbai&quot;)

# Method 4 using subset
subset(students, student_country == &quot;India&quot; &amp; student_city == &quot;Mumbai&quot;)
</code></pre></td>
  </tr>

  <!-- FILTERING USING OR -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-or-operator-in-sql-python-r/">Filtering using OR operator</a></h4></td>
    <td><pre><code class="language-SQL">SELECT * 
FROM students
WHERE student_country = 'India'
OR student_city = 'Mumbai'
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using only '|'
students[(students.student_country == 'India') | (students.student_city == 'Mumbai')]

# Method 2 using loc and '|'
students.loc[(students.student_country == 'India') | (students.student_city == 'Mumbai')]

# Method 3 using query and 'or'
students.query('student_country == &quot;India&quot; or student_city == &quot;Mumbai&quot;')
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using only '|'
students[students$student_country == &quot;India&quot; | students$student_city == &quot;Mumbai&quot;,]

# Method 2 using which
students[which(students$student_country == &quot;India&quot; | students$student_city == &quot;Mumbai&quot;),]

# Method 3 using dplyr
filter(students, student_country == &quot;India&quot; | student_city == &quot;Mumbai&quot;)

# Method 4 using subset
subset(students, student_country == &quot;India&quot; | student_city == &quot;Mumbai&quot;)
</code></pre></td>
  </tr>

  <!-- FILTERING USING BETWEEN -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-between-operator-in-sql-python-r/">Filtering using BETWEEN operator</a></h4></td>
    <td><pre><code class="language-SQL">SELECT * 
FROM degree
WHERE degree_length BETWEEN 1 AND 3
</code></pre></td>
    <td><pre><code class="language-Python">degree[degree['degree_length'].between(1, 3)]
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using only filter
degree %&gt;% filter(degree_length %in% (1:3))

# Method 2 using subset
subset(degree, degree_length %in% (1:3))

# Method 3 using between
degree %&gt;% filter(between(degree_length, 1, 3))
</code></pre></td>
  </tr>

  <!-- FILTERING USING REGEX -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-regular-expression-in-sql-python-r/">Filtering using regular expression</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT * 
FROM students
WHERE student_country REGEXP '[y|d]'

-- For Oracle
SELECT * 
FROM students
WHERE  REGEXP_LIKE (student_country, '(y|d)');
</code></pre></td>
    <td><pre><code class="language-Python">students[students['student_country']
.str.contains(r'y|d',regex=True)]
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using only grep
students[grep('(y|d)', students$student_country),]

# Method 2 using dplyr and stringr
students %&gt;% filter(str_detect(student_country, '(y|d)'))
</code></pre></td>
  </tr>

  <!-- FILTERING USING CASE SENSITIVE STRING -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-case-sensitive-string-in-sql-python-r/">Filtering using case sensitive string</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT * 
FROM students
WHERE student_country LIKE '%in%' COLLATE utf8_bin

-- For Oracle
SELECT * 
FROM students
WHERE student_country LIKE '%in%'
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using contains and lower
students[students['student_country']
.str.contains('in')]

# Method 2 using contains and case parameter
students[students['student_country']
.str.contains('in', case = True)]

# Method 3 using query and contains
students.query(
'student_country.str.contains("in")', 
engine = 'python')
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using grep
students[grep(&quot;in&quot;, students$student_country), ]

# Method using grep and ignore.case
students[grep(&quot;in&quot;, students$student_country, ignore.case=TRUE), ]

# Method 2 using str_detect
filter(students, str_detect(student_country, &quot;in&quot;))
</code></pre></td>
  </tr>

  <!-- FILTERING USING CASE INSENSITIVE STRING -->
  <tr>
    <td><h4><a href = "/programming/filtering-rows-using-case-insensitive-string-in-sql-python-r/">Filtering using case insensitive string</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT * 
FROM students
WHERE student_country LIKE '%in%'

-- For Oracle
SELECT * 
FROM students
WHERE LOWER(student_country) LIKE '%in%'
</code></pre></td>
    <td><pre><code class="language-Python"># Method 1 using contains and lower
students[students['student_country']
.str.lower().str.contains('in')]

# Method 2 using contains and case parameter
students[students['student_country']
.str.contains('in', case = False)]

# Method 3 using query and contains
students.query(
'student_country.str.lower().str.contains("in")',
engine = 'python')
</code></pre></td>
    <td><pre><code class="language-C"># Method 1 using grep and tolower
students[grep(&quot;in&quot;, tolower(students$student_country)), ]

# Method using grep and ignore.case
students[grep(&quot;in&quot;, students$student_country, ignore.case=TRUE), ]

# Method 3 using str_detect
filter(students, str_detect(tolower(student_country), &quot;in&quot;))
</code></pre></td>
  </tr>

  <!-- INNER JOIN -->
  <tr>
    <td><h4><a href = "/programming/inner-join-in-sql-python-r/">Inner join</a></h4></td>
    <td><pre><code class="language-SQL">SELECT s.student_id, s.student_name, d.degree_name
FROM students s
INNER JOIN degree d
ON s.student_id = d.student_id
</code></pre></td>
    <td><pre><code class="language-Python">pd.merge(students, degree, on = ['student_id'], how = 'inner')[['student_id', 'student_name', 'degree_name']]
</code></pre></td>
    <td><pre><code class="language-C">merge(x = students, y = degree, by = &quot;student_id&quot;)[, c(&quot;student_id&quot;, &quot;student_name&quot;, &quot;degree_name&quot;)]
</code></pre></td>
  </tr>


  <!-- LEFT JOIN -->
  <tr>
    <td><h4><a href = "/programming/left-join-in-sql-python-r/">Left join</a></h4></td>
    <td><pre><code class="language-SQL">SELECT s.student_id, s.student_name, d.degree, d.degree_country
FROM students s
LEFT JOIN degree d
ON s.student_id = d.student_id
</code></pre></td>
    <td><pre><code class="language-Python">pd.merge(students, degree, on = ['student_id'], how = 'left')[['student_id', 'student_name', 'degree_name']]
</code></pre></td>
    <td><pre><code class="language-C">merge(x = students, y = degree, by = &quot;student_id&quot;, all.x = TRUE)[, c(&quot;student_id&quot;, &quot;student_name&quot;, &quot;degree_name&quot;)]
</code></pre></td>
  </tr>


  <!-- RIGHT JOIN -->
  <tr>
    <td><h4><a href = "/programming/right-join-in-sql-python-r/">Right join</a></h4></td>
    <td><pre><code class="language-SQL">SELECT s.student_id, s.student_name, d.degree_name, d.degree_country
FROM students s
RIGHT JOIN degree d
ON s.student_id = d.student_id
</code></pre></td>
    <td><pre><code class="language-Python">pd.merge(students, degree, on = ['student_id'], how = 'right')[['student_id', 'student_name', 'degree_name']]
</code></pre></td>
    <td><pre><code class="language-C">merge(x = students, y = degree, by = &quot;student_id&quot;, all.y = TRUE)[, c(&quot;student_id&quot;, &quot;student_name&quot;, &quot;degree_name&quot;)]
</code></pre></td>
  </tr>


  <!-- FULL JOIN -->
  <tr>
    <td><h4><a href = "/programming/full-join-in-sql-python-r/">Full join</a></h4></td>
    <td><pre><code class="language-SQL">-- For MySQL
SELECT s.student_id, s.student_name, d.degree, d.degree_length FROM students s
LEFT JOIN degree d ON s.student_id = d.student_id  
UNION
SELECT s.student_id, s.student_name, d.degree, d.degree_length FROM students s
RIGHT JOIN degree d ON s.student_id = d.student_id

-- For Oracle
SELECT s.student_id, s.student_name, d.degree, d.degree_country
FROM students s
FULL JOIN degree d
ON s.student_id = d.student_id
</code></pre></td>
    <td><pre><code class="language-Python">pd.merge(students, degree, on = ['student_id'], how = 'outer')[['student_id', 'student_name', 'degree_name']]
</code></pre></td>
    <td><pre><code class="language-C">merge(x = students, y = degree, by = &quot;student_id&quot;, all = TRUE)[, c(&quot;student_id&quot;, &quot;student_name&quot;, &quot;degree_name&quot;)]
</code></pre></td>
  </tr>

</table>

The End.