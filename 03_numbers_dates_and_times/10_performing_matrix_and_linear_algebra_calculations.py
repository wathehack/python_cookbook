import numpy as np
import numpy.linalg


# The NumPy library has a matrix object that can be used for this purpose.
# More operations can be found in the numpy.linalg subpackage.
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# Return transpose.
print(m.T)
# Return inverse.
print(m.I)
# Create a vector and multiply.
v = np.matrix([[2], [3], [4]])
print(v)
print(m * v)

# Determinant.
print(numpy.linalg.det(m))
# Eigenvalues.
print(numpy.linalg.eigvals(m))
# Solve for x in mx = v.
x = numpy.linalg.solve(m, v)
print(x)
print(m * x)
print(v)
