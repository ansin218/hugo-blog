#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 21:43:38 2019

@author: ankurs
"""

import pandas as pd

students = pd.DataFrame()
students['student_id'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
students['student_name'] = ['John', 'Hari', 'Ali', 'Jenny', 'Lisa', 'Priya', 'Wong', 'Julius', 'Alonso', 'Noor']
students['student_city'] = ['Atlanta', 'Mumbai', 'Dubai', 'Berlin', 'Berlin', 'Delhi', 'Beijing', 'Rome', 'Atlanta', 'London']
students['student_country'] = ['USA', 'India', 'UAE', 'Germany', 'Germany', 'India', 'China', 'Italy', 'USA', 'UK']

degree = pd.DataFrame()
degree['degree_id'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
degree['student_id'] = [1, 2, 2, 2, 3, 4, 4, 7, 7, 7, 10, 6, 6]
degree['degree_name'] = ['B. Arts', 'B. Tech', 'MS', 'PhD', 'B. Sc.', 'B. Sc.', 'M. Sc.', 'BS', 'MS', 'PhD', 'BE', 'BE', 'ME']
degree['degree_country'] = ['USA', 'India', 'USA', 'USA', 'Germany', 'Switzerland', 'Germany', 'China', 'Australia', 'USA', 'UK', 'India', 'India']
degree['degree_length'] = [3, 4, 2, 5, 4, 4, 3, 3, 1, 3, 4, 4, 2]

# Method 1 using len
#len(students)

# Method 2 using shape
#students.shape[0]

# Method 3 using count
#students['student_id'].count()

import timeit

def foobar():
    students.shape[1]

print(timeit.timeit(stmt = foobar, number = 100000))