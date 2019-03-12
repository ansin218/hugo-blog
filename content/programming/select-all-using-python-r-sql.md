---
title: "Select All Using Python, R and SQL"
date: 2019-03-11T14:53:25+01:00
draft: true
---

#### Table Students:

| Student_ID | Student_Name | Student_City | Student_Country |
| ---------- | ------------ | ------------ | --------------- |
| 1          | John         | Atlanta      | USA             |
| 2          | Hari         | Mumbai       | India           |
| 3          | Ali          | Dubai        | UAE             |
| 4          | Jenny        | Berlin       | Germany         |
| 5          | Lisa         | Berlin       | Germany         |
| 6          | Priya        | Delhi        | Mumbai          |
| 7          | Wong         | Beijing      | China           |
| 8          | Julius       | Rome         | Italy           |
| 9          | Alonso       | Atlanta      | USA             |
| 10         | Noor         | London       | UK              |

## Select All Records Using SQL:

```SQL
SELECT * FROM Students
```

#### Table Degree:

| Student_Degree_ID | Student_ID | Degree  | Degree_Country | Degree_Length |
| ----------------- | ---------- | ------- | -------------- | ------------- |
| 1                 | 1          | B. Arts | USA            | 3             |
| 2                 | 2          | B. Tech | India          | 4             |
| 3                 | 2          | MS      | USA            | 2             |
| 4                 | 2          | PhD     | USA            | 5             |
| 5                 | 3          | B. Sc.  | Germany        | 4             |
| 6                 | 4          | B. Sc.  | Switzerland    | 4             |
| 7                 | 4          | M. Sc.  | Germany        | 3             |
| 8                 | 7          | BS      | China          | 3             |
| 9                 | 7          | MS      | Australia      | 1             |
| 10                | 7          | PhD     | USA            | 3             |
| 11                | 10         | BE      | UK             | 4             |
| 12                | 6          | BE      | India          | 4             |
| 13                | 6          | ME      | India          | 2             |

Table in HTML:

<table>
<tr>
<td>Student_Degree_ID</td>
<td>Student_ID</td>
<td>Degree</td>
<td>Degree_Country</td>
<td>Degree_Length</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>B. Arts</td>
<td>USA</td>
<td>3</td>
</tr>
<tr>
<td>2</td>
<td>2</td>
<td>B. Tech</td>
<td>India</td>
<td>4</td>
</tr>
<tr>
<td>3</td>
<td>2</td>
<td>MS</td>
<td>USA</td>
<td>2</td>
</tr>
<tr>
<td>4</td>
<td>2</td>
<td>PhD</td>
<td>USA</td>
<td>5</td>
</tr>
<tr>
<td>5</td>
<td>3</td>
<td>B. Sc.</td>
<td>Germany</td>
<td>4</td>
</tr>
<tr>
<td>6</td>
<td>4</td>
<td>B. Sc.</td>
<td>Switzerland</td>
<td>4</td>
</tr>
<tr>
<td>7</td>
<td>4</td>
<td>M. Sc.</td>
<td>Germany</td>
<td>3</td>
</tr>
<tr>
<td>8</td>
<td>7</td>
<td>BS</td>
<td>China</td>
<td>3</td>
</tr>
<tr>
<td>9</td>
<td>7</td>
<td>MS</td>
<td>Australia</td>
<td>1</td>
</tr>
<tr>
<td>10</td>
<td>7</td>
<td>PhD</td>
<td>USA</td>
<td>3</td>
</tr>
<tr>
<td>11</td>
<td>10</td>
<td>BE</td>
<td>UK</td>
<td>4</td>
</tr>
<tr>
<td>12</td>
<td>6</td>
<td>BE</td>
<td>India</td>
<td>4</td>
</tr>
<tr>
<td>13</td>
<td>6</td>
<td>ME</td>
<td>India</td>
<td>2</td>
</tr>
</table>




asdas

<table>
  <tr>
    <td></td>
    <td><b>XLSX</b></td>
    <td><b>CSV</b></td>
    <td><b>Pickle</b></td>
    <td><b>HDF5</b></td>
  </tr>
  <tr>
    <td><b>Execution Time</b></td>
    <td>4m48s</td>
    <td>22.172s</td>
    <td>786ms</td>
    <td>1.221s</td>
  </tr>
  <tr>
    <td><b>Storage Size</b></td>
    <td>54.5MB</td>
    <td>107.9MB</td>
    <td>77.1MB</td>
    <td>78.1MB</td>
  </tr>
</table>
