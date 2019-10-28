---
title: "Reading Pickle File in R"
date: 2018-11-01T20:27:56+01:00
description: "How to read a pickle file from Pandas in Python to R"
image: "https://images2.imgbox.com/0f/d5/vFDtd2oK_o.jpg"
url: "/programming/data-analysis/reading-pickle-file-in-r/"
---

Recently, I was asked if I could share a particular dataset with some colleague of mine who wanted to test it in an R environment. Although this sounds straightforward, the problem was that the dataset from Pandas dataframe was stored in *.pickle* format. Now, at this stage, one possible solution was to load it in Python, save it as a CSV file and load the CSV file in an R environment. However, I came up with a possibility to achieve this without involving any CSV files.

Let us assume you have a file called `dataset.pickle` in a folder called `tsa`

[Reticulate] (https://github.com/rstudio/reticulate) is an R package to help interface R with Python. Install this package with the command:

```R
install.packages('reticulate')
```

Now, create a Python file with the following lines:

```Python
import pandas as pd

def read_pickle_file(file):
    pickle_data = pd.read_pickle(file)
    return pickle_data
```

Create an R file with the following lines:

```R
require("reticulate")

source_python("pickle_reader.py")
pickle_data <- read_pickle_file("C:/tsa/dataset.pickle")
```

You must now be able to read the data from the pickle file in your R environment.