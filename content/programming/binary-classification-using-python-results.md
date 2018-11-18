---
title: "Binary Classification Using Python: Results"
date: 2018-11-17T01:14:21+01:00
description: "Confusion Matrix, Accuracy, Precision, Recall, F1, ROC AUC Curve"
---

In the previous part of this series, we had built our model. We now want to check how our model has performed. We will look into different metrics to conclude how good or bad our model is.

### Confusion Matrix

```Python
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_true, y_pred))
```

Result:

```
[[ 4608  3233]
 [ 1670 23050]]
```

If you are wondering what these numbers are, this reference image from Tarek Atwan's blog can help.

![alt text](https://images2.imgbox.com/ef/6b/qe4x1wHb_o.png "Confusion Matrix")

The diagonal from the top left to bottom right denotes what the model got right while the other diagonal tells us where our model went wrong. Let us look into the terms TP, TN, FP and FN in the context of our dataset.

__True Positive:__ We predicted them to earn less than 50k, and they actually earn less than 50k

__True Negative:__ We predicted them to earn more than 50k, and they actually earn more than 50k

__False Positive:__ We predicted them to earn less then 50k, but they were actually earning more than 50k

__False Negative:__ We predicted them to earn more than 50k, but they were actually earning less than 50k


### Accuracy

Accuracy can be defined as the number of correctly predicted instances to the total number of instances.

```Python
from sklearn.metrics import accuracy_score

print('Accuracy Score of Model: ', accuracy_score(y_true, y_pred) * 100)
```

Result:
```
Accuracy Score of Model:  84.94210865759652
```

Although an accuracy of 84.92 seems good, accuracy must not be the only thing to conclude if our model is doing well. It is good to also compute precision and recall. The image below from Wikipedia illustrates precision and recall.

![alt text](https://images2.imgbox.com/40/bf/wV0GuOTa_o.png "Precision and Recall")

### Precision

Precision = (TP) / (TP + FP)

```Python
from sklearn.metrics import precision_score

print('Precision Score of Model: ', precision_score(y_true, y_pred) * 100)
```
Result:

```
Precision Score of Model:  87.69927329452498
```

### Recall

Recall = (TP) / (TP + FN)

```Python
from sklearn.metrics import recall_score

print('Recall Score of Model: ', recall_score(y_true, y_pred) * 100)
```

Result:

```
Recall Score of Model:  93.24433656957929
```

F1:

A metric that combines precision and recall by considering the harmonic mean between both.

F1 = (2 * Precision * Recall) / (Precision + Recall)

```Python
from sklearn.metrics import f1_score

print('F1 Score of Model: ', f1_score(y_true, y_pred) * 100)
```

Result:
```
F1 Score of Model:  90.38683998980452
```

### ROC AUC Score:

This computes the area under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores. More the area under curve, better it is.

```Python
from sklearn.metrics import roc_auc_score

print('ROC AUC Score of Model: ', metrics.roc_auc_score(y_true, y_pred) * 100)
```

Result:

```
ROC AUC Score of Model: 76.00617542673581
```

The above metrics show that our model is doing fairly well. Congratulations on building your first model!