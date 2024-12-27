'''
Numpy is a fundamental package which is used for scientific computing in Python.
It is a general-purpose array-processing package.
It provides a high-performance multidimensional array object, and tools for working with these arrays.

This encapsulated n dimensional arrays of homogenous data types, with many operations being performed in compiled code for performance.
 Numpy is based in c (for speed) and a wrapper is wounded over it for python(syntax easy)

Numpy array vs Python Lists
-> size of numpy array is fixed while python list is dynamic
-> numpy array is faster than python list
-> numpy array is homogenous while python list is heterogenous
-> no referential integrity in numpy array , the values are directly added


'''


# np.array
import numpy as np





# CREATING NUMPY ARRAYS

a = np.array([1,2,3])  # array
print(a)


# 2D and 3D
b = np.array([[1,2,3],[4,5,6]]) # matrix
print(b)
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])  # tensor
print(c)

# to take float type numpy array
np.array([1,2,3],dtype=float)

# to take boolean type numpy array
np.array([1,2,0],dtype=bool)     # True, True, false

# to take complex type numpy array
np.array([1,2,3],dtype=complex)  # 1+0i , 2+0i


# to take range
np.arange(10)  # 0 to 9
np.arange(1,11,2) # 1 to 10 with step 2

# reshape
# the normal arange returns an single 1d array in the form of list
# but if we want to convert it into 2d or 3d array we can use reshape
np.arange(1,13).reshape(3,4)  # 3 rows and 4 columns
np.arange(1,13).reshape(4,3)  # 4 rows and 3 columns
# the poduct of rows and columns should be equal to the number of elements in the array
np.arange(1,13).reshape(5,5)  # not possible

# to create matrix of ones and zeroes
np.ones((3,4)) # 3 rows and 4 columns of all 1
np.zeros((3,4)) # 3 rows and 4 columns of all 0
np.random.random((3,4)) # 3 rows and 4 columns of random numbers

# linspace -> linear space
np.linspace(1,5,10)  # 10 numbers between 1 and 5

# identity matrix
np.identity(3) # 3x3 identity matrix








# ARRAY ATTRIBUTES

a1=np.arange(10)
a2=np.arange(12 , dtype=float).reshape(3,4)





