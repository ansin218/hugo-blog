---
title: "Pandas Data Export Comparison"
date: 2018-11-07T16:21:33+01:00
description: "Compare benchmarks of XLSX, CSV, Pickle and HDF5 files"
image: "https://images2.imgbox.com/75/d8/befrNwoK_o.jpg"
---

In this post, we look at the common data export options in Pandas using Python and compare them on the basis of execution time and storage size. The file formats used for comparison are XLSX, CSV, Pickle and HDF5.

First, let us consider a dataset with more than 1 million records to perform this task. The dataset I am using has the following structure.

```Python
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1009989 entries, 0 to 1034143
Data columns (total 12 columns):
FEATURE1         1009989 non-null int64
FEATURE2         1009989 non-null int64
FEATURE3         1009989 non-null object
FEATURE4         1009989 non-null object
FEATURE5         1009989 non-null object
FEATURE6         1009989 non-null object
FEATURE7         1009989 non-null float64
FEATURE8         1009989 non-null float64
FEATURE9         1009989 non-null int64
FEATURE10        1009989 non-null datetime64[ns]
FEATURE11        1009989 non-null datetime64[ns]
FEATURE12        1009989 non-null datetime64[ns]
dtypes: datetime64[ns](3), float64(2), int64(3), object(4)
memory usage: 100.2+ MB
```

The dataset above has columns with different data types (int, object, float, datetime) that a data analyst or data scientist typically encounters. The following lines can be used to export your dataset in different formats.

```Python
import pandas as pd
from pandas import ExcelWriter

# Excel
writer = ExcelWriter('test-x.xlsx')
x.to_excel(writer, index = False, sheet_name = 'Sheet1')
writer.save()

# CSV
x.to_csv('test-c.csv')

# Pickle
x.to_pickle('test-p.pickle')

# HDF5
x.to_hdf('test-h.h5', key = 's')
```

Now, to export them as efficiently as possible, let us have a look at some numbers.

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

Pickle formats perform the best in terms of time but XLSX in terms of storage. However, loading the entire dataset on Microsoft Excel or other Excel applications can at times be infeasible due to large size. I usually save my datasets in Pickle format as it fits my needs better compared to HDF5, and use CSV only when I have to share the dataset with someone who is working in a different environment.