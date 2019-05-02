---
title: "Cheatsheet for SQL, Python and R"
date: 2019-04-21T11:38:17+02:00
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
    <td><h4><a href = "https://ankuroh.com/programming/python-r-sql-cheatsheet/">Select All Records</a></h4></td>
    <td><pre>SELECT * FROM table<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
    <td><pre>df<span class = "copy-to-clipboard"></pre></td>
  </tr>
  <tr>
    <td><a href = "https://ankuroh.com/programming/">Count</a></td>
    <td><pre>SELECT Student_Country, Count(*)
FROM Students
GROUP BY Student_Country<span class = "copy-to-clipboard"></pre></td>
    <td><pre>students[['student_country']].apply(lambda x: x.value_counts())<span class = "copy-to-clipboard"></pre></td>
    <td><pre>count(students, "student_country")<span class = "copy-to-clipboard"></pre></td>
  </tr>
</table>


#### Table Degree:

| Method            | SQL | Python  | R |
| ----------------- | ---------- | ------- | -------------- |
| 1                 | 1          | B. Arts | USA            |
| 2                 | 2          | B. Tech | India          |
| 3                 | 2          | MS      | USA            |
| 4                 | 2          | PhD     | USA            |
| 5                 | 3          | B. Sc.  | Germany        |
| 6                 | 4          | B. Sc.  | Switzerland    |
| 7                 | 4          | M. Sc.  | Germany        |
| 8                 | 7          | BS      | China          |
| 9                 | 7          | MS      | Australia      |
| 10                | 7          | PhD     | USA            |
| 11                | 10         | BE      | UK             |
| 12                | 6          | BE      | India          |
| 13                | 6          | ME      | ```SELECT * FROM Students WHERE HAVING ORDER BY ```|