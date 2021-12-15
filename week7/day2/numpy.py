# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:32:17 2021

@author: Yasaar Mauthoor
"""

"""Part1-basic"""
""" Please solve the following excercises
 Good Luck!
 1. Import the numpy package under the name `np`
 2. Print the numpy version
 hint: search on Google "numpy version", the first entry.
 3. Create a vector of zeros with the size 10
 hint: use np.zeros()
 4. How to find the memory size of any array
 hint: itemsize returns the size in memory of each element
 5. How to get the documentation of the numpy add function from the IPython console?
 hint: try "?" before the function name
 6. Create a vector of zeros with the size 10 but the fifth value which is 1
 7. Create a vector with values ranging from 10 to 49 ( ) ★☆☆
 hint: arange
 8. Reverse a vector (first element becomes last) ( ) ★☆☆
 hint: [::-1]
 9. Create a 3x3 matrix with values ranging from 0 to 8 ( ) ★☆☆
 hint: reshape
 10. Find indices of non-zero elements from \[1,2,0,0,4,0\] ( ) ★☆☆
 hint: nonzero
 11. Create a 3x3 identity matrix ( )★☆☆
 hint: the best numpy documentation is in the scipy website :)
 try https://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html
 12. Create a 3x3x3 array with random values ( )★☆☆
 hint:  https://docs.scipy.org/doc/numpy/reference/routines.random.html
 13. Create a 10x10 array with random values and find the minimum and maximum values 
 hint:  a.min,a.max 
 14. Create a random vector of size 30 and find the mean value 
 hint: a.mean 
 15. Create a 2d array with 1 on the border and 0 inside 
 hint: ones()
 hint2:  for an array a, which elements are chosen by a[1:-1] ?
 16. How to add a border (filled with 0's) around an existing array? 
 hint: https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html
 17. What is the result of the following expression? ( )★☆☆
```python
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1
```
 hint 1: nan is not a number
 hint 2: try printing the expressions to see what is printed
 18. Create a 5x5 matrix with values 1,2,3,4,7 on the diagonal 
 hint: np.diag
 19. Create a 8x8 matrix and fill it with a checkerboard pattern 
 hint1:  slicing an array you can use - list[start:end:step]
 hint2:  [::2] - for even.  [1::2] - for odd
 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
 hint:  https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.unravel_index.html"""
 
 #1
import numpy as np
# #2
# print (np.__version__)
# #3
# z = [0] * 10
# print(z)
# #4
# # z_size = z.itemsize
# # print (z_size)
# #5

# #6
# x=np.zeros(10)
# x[4]=1
# #7
# v = np.arange(10,49)
# print("Original vector:")
# print(v)

# #8
# print(v[::-1])
# #9
# ar = np.arange(0,9)
# ar = np.reshape(ar,(3,3))
#10
r = np.array([1,2,0,0,4,0])
np.nonzero(r)

#11







