# -*- coding: utf-8 -*-
"""
# Exercise 1.1: Introduction

Advanced Machine Learning for KCS

by Stefan Heinrich, Stella Grasshof, Laura Weihl
with material by Kevin Murphy

All info and static material: https://learnit.itu.dk/course/view.php?id=3021295
-------------------------------------------------------------------------------

## Introduction to Python basics

"""


# Import libraries
from __future__ import print_function  # special import for python 2.7
import numpy as np


"""
Optional Revision: Get familiar with plain python 

Optional Task: go through the documentation of python (at least make some bookmarks) 
and get familiar with basic expressions:
- create a column vector B with three rows of a single number 1-3
- create a 3x3 matrix C with numbers 1-9
- observe the effect of accessing the matrix differently: 
C[:,2] C[:,1:3] C[:,2:3] C[2,3,:]

https://www.python.org/about/gettingstarted/
important: always adhere to the python pep-8 style:
https://www.python.org/dev/peps/pep-0008/
"""
B = [1, 2, 3]
C = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#x1 = C[:, 2]
x1 = C[:][2]
x1
x2 = C[:][1:3]
x2
x3 = C[:][2:3]
x3
x4 = C[2][3][:]
x4

a = 7
print(a)


"""
Optional Revision: Get familiar the power of packages at the example of numpy 

Optional Task: go through the documentation of numpy 
and learn how matrix expressions and representations are different:
- create a horizontal numpy array E with three rows of a single number 1-3
- create a 2-dimensional numpy array (3x3 matrix) F with numbers 1-9
- figure out how you can access the numpy array similar to matrix C
- figure out how you can print the shape and content of F efficiently
- create a numpy array (3x1 vector) G of ones
- create a 2-dimensional numpy array (2x3 matrix) H of zeros
- concatenate two numpy arrays of random numbers into array K
- conduct basic operations on your array K: sum, max, mean

https://numpy.org/learn/
"""
E = np.array([1, 2, 3])

d = np.float(42)
print(d)

