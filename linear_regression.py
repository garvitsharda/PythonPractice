# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

# SciPy stands for Scientific Python.
# It provides more utility functions for optimization, stats and signal processing.

import matplotlib.pyplot as plt
from scipy import stats

# Create the arrays that represent the values of the x and y axis:

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

# The scatter() function plots one dot for each observation. 
# It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Refrence Link : https://www.w3schools.com/python/python_ml_linear_regression.asp
