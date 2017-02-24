import numpy as np


# For any heavy computation involving arrays, use the NumPy library. The major
# feature of NumPy is that it gives Python an array object that is much more
# efficient and better suited for mathematical calculation than a standard
# Python list.
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
print(x + y)
try:
    x + 10
except Exception as e:
    print(e)

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)


def f(x):
    return 3 * x**2 - 2 * x + 7
print(f(ax))

print(np.sqrt(ax))
print(np.cos(ax))

# Under the covers, NumPy arrays are allocated in the same manner as in C or
# Fortran. Namely, they are large, contiguous memory regions consisting of a
# homogenous data type. Because of this, it's possible to make arrays much
# larger than anything you would normally put into a Python list.
grid = np.zeros(shape=(10000, 10000), dtype=float)
grid += 10

# One extremely notable aspect of NumPy is the manner in which it extends
# Python's list indexing functionality, especially with multidimensional
# arrays.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# Select row 1.
print(a[1])
# Select column 1.
print(a[:, 1])
# Select a subregion and change it.
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
# Broadcast a row vector across an operation on all rows.
print(a + [100, 101, 102, 103])
# Conditional assignment on an array.
print(np.where(a < 10, a, 10))
