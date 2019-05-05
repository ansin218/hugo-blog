---
title: "Binary Classification Using Python: Data Cleaning"
date: 2018-11-17T13:24:19+01:00
description: "Reading, cleaning and handling missing data"
image: "https://images2.imgbox.com/78/a4/fvIOpDDW_o.jpg"
draft: true
---

In this tutorial, we will read the data, analyze how it looks and clean it accordingly using a library called [Pandas](https://pandas.pydata.org/). There are two ways to read the data: reading directly from the URL or reading it locally after downloading it from the URL.

The data from the URL can be read and stored in a dataframe by doing the following:

```Python
import pandas as pd
import io
import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
s = requests.get(url).content
df1 = pd.read_csv(io.StringIO(s.decode('utf-8')), header = None)
```

Alternatively, you can also download the data and read it using:

```Python
df1 = pd.read_csv('Path/To/Data', header = None)
```

On carefully looking at the data, you will notice that our dataset has no headers. However, this problem can be solved by assigning relevant headers to our dataset by doing:

```Python
df1.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
               'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss',
               'hours-per-week', 'native-country', 'class']
```

Now that we have our data with relevant column names ready, we can check if there are any empty or `NaN` values in the dataset:

```Python
df1.isnull().values.any()
```

For this dataset, it returns `False`, which means there are no empty/null values in the dataset. However, if one checks the dataset, values with `?` can be found. This denotes that there is something missing. An example is shown below.

![alt text](https://images2.imgbox.com/98/0f/Asg3YQVb_o.png "Missing Data")

We will now replace all the ? in our data with `NaN` values.

```Python
df1 = df1.replace(' ?', np.nan)
```

Let us see how to deal with `NaN` values because they are common in many datasets. Let us check which columns have the `NaN` values.

```Python
df1.columns[df1.isna().any()].tolist()
```

This returns:

```
['workclass', 'occupation', 'native-country']
```

There are many things you can do with such `NaN` data. You can go ahead with the model excluding such records or replace them with mean, median or mode, or any other value, depending on the problem statement. For this problem, we will just replace them with most common value of the pertinent column. In other words, we will replace the missing value with the mode value of the column.

```Python
for column in ['workclass', 'occupation', 'native-country']:
    df1[column].fillna(df1[column].mode()[0], inplace = True)
```

We can also look into how our data is split into different classes:

```Python
df1['class'].value_counts()
```

This dataset is clearly imbalanced with around 24k of the 32k records belonging to one particular class. However, we will go ahead building our model without considering this imbalance. I will cover the topic of building balanced datasets in another blog post.

In the next part of this series, we will perform some feature engineering techniques.