---
title: "Binary Classification Using Python: Introduction"
date: 2018-11-17T13:31:01+01:00
description: "Introduction to machine learning techniques and logistic regression"
image: "https://images2.imgbox.com/78/a4/fvIOpDDW_o.jpg"
---

This tutorial is a 5 part series which goes through the basics of building a simple machine learning model to perform binary classification. Although this tutorial is aimed at beginners, basic background in statistics and programming can be beneficial.

[Binary Classification Using Python: Introduction | Introduction to machine learning techniques and logistic regression](https://ankuroh.com/programming/binary-classification-using-python-introduction/)
[Binary Classification Using Python: Data Cleaning | Reading, cleaning and handling missing data](https://ankuroh.com/programming/binary-classification-using-python-data-cleaning/)
[Binary Classification Using Python: Feature Engineering | Feature engineering, feature selection and feature scaling](https://ankuroh.com/programming/binary-classification-using-python-feature-engineering/)
[Binary Classification Using Python: Model Construction | Training, testing and k-fold cross validation of model](https://ankuroh.com/programming/binary-classification-using-python-model-construction/)
[Binary Classification Using Python: Results | Confusion Matrix, Accuracy, Precision, Recall, F1, ROC AUC Curve](https://ankuroh.com/programming/binary-classification-using-python-results/)

### Machine Learning

Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to learn from data, without being explicitly programmed. Learning can be classified into 3 types.

__Supervised Learning__: There are classes assigned for output variables and algorithms learn to predict the output from the input data.

__Unsupervised Learning__: There are not classes for output variables and algorithms learn to come up with a structure from the input data.

__Semi-Supervised Learning__: Partially labeled data for output variables and requires a mixture of supervised and unsupervised learning techniques to be used.

There are many algorithms to perform classification using supervised learning methods such as logistic regression, decision trees and random forests, to mention a few. In this tutorial, we will see how to perform binary classification using logistic regression in Python.

### Logistic Regression

Logistic regression is used to explain the relationship between one dependent binary variable and one or more independent variables. Below, you can see how the logistic regression formula looks like. The probability, *p*, of someone/something belonging to a particular class is given by:

![alt text](https://images2.imgbox.com/aa/d9/M0IAUMTa_o.png "Logistic Regression Formula")

where *b<sub>0</sub>* is the intercept, and *b<sub>1</sub>, b<sub>2</sub>, .., b<sub>p</sub>* are the coefficients of features *x<sub>1</sub>, x<sub>2</sub>, .., x<sub>p</sub>*, respectively. The image below shows how a logistic curve looks like.

![alt text](https://images2.imgbox.com/c6/0d/gZFdw48D_o.png "Logistic Curve")

In this tutorial, we will consider a dataset where we need to predict if a person earns more than 50k using a given set of features. You can download the dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult).