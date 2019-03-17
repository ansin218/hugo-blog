---
title: "Binary Classification Using Python: Feature Engineering"
date: 2018-11-17T13:02:10+01:00
description: "Feature engineering, feature selection and feature scaling"
image: "https://images2.imgbox.com/78/a4/fvIOpDDW_o.jpg"
---

Feature engineering is a broad topic and can demand a separate series in itself. Wikipedia quotes, Feature engineering is the process of using domain knowledge of the data to create features that make machine learning algorithms work. However, we will go through a few things with regards to choosing a combination of features to give us the best result. Currently, our dataset looks like this:

```Python
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 32561 entries, 0 to 32560
Data columns (total 15 columns):
age               32561 non-null int64
workclass         32561 non-null object
fnlwgt            32561 non-null int64
education         32561 non-null object
education-num     32561 non-null int64
marital-status    32561 non-null object
occupation        32561 non-null object
relationship      32561 non-null object
race              32561 non-null object
sex               32561 non-null object
capital-gain      32561 non-null int64
capital-loss      32561 non-null int64
hours-per-week    32561 non-null int64
native-country    32561 non-null object
class             32561 non-null object
dtypes: int64(6), object(9)
memory usage: 3.7+ MB
```

We will drop two attributes from this dataset: `class` because this is the target variable and `fnlwgt` because we do not have any description for this attribute and cannot conclude anything from results, if any. To do so, we will do:

```Python
X = df1.drop(['class', 'fnlwgt'], axis = 1)
```

From the other set of features that are categorical (shown as type object), we can form a set of dummy variables which corresponds to class `0` or `1`. To do so, write:

```Python
dcList = ['workclass', 'education', 'marital-status', 'occupation', 'relationship',
          'race', 'sex', 'native-country']
X = pd.get_dummies(data = X, columns = dcList)
```

Earlier we have 13 features but now we have 104. The question now arises, do we need all the 104 features?

### Feature Selection

In machine learning and statistics, feature selection (variable selection, attribute selection or variable subset selection) is the process of selecting a subset of relevant features for constructing our prediction model. To perform feature selection, I will use a library called [feature-selector](https://github.com/WillKoehrsen/feature-selector/).

The FeatureSelector has five functions for identifying columns to remove: identify missing values, identify variables with single unique values, identify collinear variables, identify variables with zero importance and identify variables with low importance. Import the library and create an instance with the features and target variable. In the code snippets below, I have mostly considered the parameter values from the documentation. You are free to play with different numbers to see how things change.

```Python
from feature_selector import FeatureSelector

fs = FeatureSelector(data = X, labels = df1['class'])
```

#### Identify Features With Missing Values

```Python
fs.identify_missing(missing_threshold = 0.6)
missing_features = fs.ops['missing']
```

Result:

```
0 features with greater than 0.60 missing values.
```

#### Identify Features With Single Unique Values

```Python
fs.identify_single_unique()
single_unique = fs.ops['single_unique']
```

Result:

```
0 features with a single unique value.
```

In cases like the dataset having columns such as Email ID, Customer ID, and other similar attributes, this technique of finding variables with unique values can help.

#### Identify Features With Collinearity

```Python
fs.identify_collinear(correlation_threshold = 0.75)
correlated_features = fs.ops['collinear']
```

Result:

```
3 features with a correlation magnitude greater than 0.75.
```

#### Identify Features With Zero Importance

```Python
fs.identify_zero_importance(task = 'classification', eval_metric = 'auc', n_iterations = 10, early_stopping = True)
zero_importance_features = fs.ops['zero_importance']
```

Result:

```
Training Gradient Boosting Model

Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[195]   valid_0's binary_logloss: 0.265558      valid_0's auc: 0.935227
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[199]   valid_0's binary_logloss: 0.276727      valid_0's auc: 0.927433
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[223]   valid_0's binary_logloss: 0.273206      valid_0's auc: 0.931405
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[202]   valid_0's binary_logloss: 0.289187      valid_0's auc: 0.922156
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[252]   valid_0's binary_logloss: 0.284854      valid_0's auc: 0.923279
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[262]   valid_0's binary_logloss: 0.274284      valid_0's auc: 0.929912
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[212]   valid_0's binary_logloss: 0.277053      valid_0's auc: 0.929317
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[171]   valid_0's binary_logloss: 0.275693      valid_0's auc: 0.928876
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[171]   valid_0's binary_logloss: 0.284055      valid_0's auc: 0.927447
Training until validation scores don't improve for 100 rounds.
Early stopping, best iteration is:
[293]   valid_0's binary_logloss: 0.265304      valid_0's auc: 0.930087

16 features with zero importance after one-hot encoding.
```

#### Identify Features With Low Importance

```Python
fs.identify_low_importance(cumulative_importance = 0.99)
low_importance_features = fs.ops['low_importance']
```

Result:

```
66 features required for cumulative importance of 0.99 after one hot encoding.
38 features do not contribute to cumulative importance of 0.99.
```

We will now append all the features that can be discarded by appending it to a huge list and dropping it from our features dataframe that will be eventually fed to the model.

```Python
useless_features_list = list()
useless_features_list = useless_features_list + correlated_features
useless_features_list = useless_features_list + zero_importance_features
useless_features_list = useless_features_list + low_importance_features
useless_features_list = list(set(useless_features_list))
X = X.drop(useless_features_list, axis = 1)
```

### Feature Scaling

Raw data can sometimes have range of values varying widely which can lead to some objective functions not working properly. Hence, we need to normalize our data. This helps in each feature contribute more or less proportionately to the final distance. In addition, methodologies such as gradient descent also helps in faster convergence with feature scaling than without.

It is to be noted that feature scaling may not necessarily lead to better results always. Another important factor before performing feature scaling is to see how the distribution of the dataset is. For example, a dataset with normal distribution may require Standard Scaling. MinMax Scaler is another popular scaling algorithm used when the data is not normally distributed, and helps in shrinking values between 0 and 1 or 1 and -1 depending on the data.

Since our data is not normally distributed and we will use a regularization technique later, we will use Robust Scaler which is like MinMax Scaler but helps us deal with outliers. To do so, we will use a library called [scikit-learn](https://scikit-learn.org/stable/).

```Python
from sklearn.preprocessing import RobustScaler
import numpy as np

X = X.values.astype(np.float)
scaler = RobustScaler()
X = scaler.fit_transform(X)
```

In the next part of this series, we will dive into feeding our scaled features with target variable to build our model using cross validation.