import cmath
import numpy as np
import math


# Complex numbers can be specified using the complex(real, imag) function or
# by floating-point numbers with a j suffix.
a = complex(2, 4)
b = 3 - 5j
print(a, b)
print(a.real)
print(a.imag)
print(a.conjugate())
print(a + b)
print(a * b)
print(a / b)
print(abs(a))

# To perform additional complex-valued functions such as sines, cosines, or
# square roots, use the cmath module.
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

# Most of Python's math-related modules are aware of complex values, such as
# numpy.
a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
print(a)
print(a + 2)
print(np.sin(a))

# Python's standard mathematical functions do not produce complex values by
# default.
try:
    math.sqrt(-1)
except Exception as e:
    print(e)

# Explicitly use cmath or declare the use of a complex type in libraries that
# know about them.
print(cmath.sqrt(-1))
