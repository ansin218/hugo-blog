---
title: "Binary Classification Using Python: Model Construction"
date: 2018-11-17T12:03:33+01:00
description: "Training, testing and k-fold cross validation of model"
---

Now that we have our features selected and scaled, we will go ahead constructing our logistic regression model. Datasets our can be split into two or three parts while creating the model. They are namely train set, validation set and test set.

__Train Set:__ The dataset used to learn the patterns and build our prediction algorithm.

__Validation Set:__ The dataset that is used to check the performance of the prediction model created using the training set.

__Test Set:__ The dataset, which is unseen, on which the prediction model will be tested.

In this tutorial, we will perform K-Fold Cross Validation which splits the dataset into training set and testing set over multiple iterations; in this case, `K` iterations. A simple graphical illustration of cross validation is shown below.

![alt text](https://scikit-learn.org/stable/_images/sphx_glr_plot_cv_indices_002.png "K-Fold Cross Validation")

To do so, we will also create a target variable like this:

```Python
y_true = np.where(df1['class'] == ' <=50K', 1, 0)
```

To understand what the above statement means, anyone earning more than 50k is what we will try predicting and hence assign classes of `1 ` and `0` that correspond to less than 50k and more than 50k. `y_true` is a common terminology for the ground truth which is how our actual event turned out to be. `y_pred` is another common terminology for predicting `y_true` as accurately as possible.

Let us create a variable `y_pred` by copying `y_true` but will eventually replace `y_pred` with predicted values.

```Python
y_pred = y_true.copy()
```

We will perform a 5-Fold cross validation. To do so, write:

```Python
from sklearn.model_selection import KFold

kf = KFold(n_splits = 5, shuffle = True)
```

And now, for each iteration, we will have a training set and testing set on which the Logistic Regression will be performed. The code looks like:

```Python
from sklearn.linear_model import LogisticRegression

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train = y_true[train_index]
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_pred[test_index] = clf.predict(X_test)
```

At this point, it would be nice to see what all parameters the LogisticRegression() boasts of and can be fine tuned:

```Python
LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver=’warn’, max_iter=100, multi_class=’warn’, verbose=0, warm_start=False, n_jobs=None)
```

To go through all these parameters is beyond the scope of this tutorial. Hence, I would request readers to check out the [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) to dive further into what they all mean. Similarly, you can also check out other algorithms to explore further.

Like classes, you can also predict probabilites by replacing `clf.predict` with `clf.predict_proba`.

To know the intercepts and coefficients of the logistic regression model, you can do:

```Python
print(clf.coef_)
print(clf.intercept_)
```

Now that we have `y_pred` and `y_true`, in the final part of the tutorial, we will see how our model has fared.