from decimal import Decimal, localcontext
import math


# Performing accurate calculations with decimal numbers.
a = 4.2
b = 2.1
print(a + b)

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

# A major feature of decimal is that it allows you to control different
# aspects of calculations, including number of digits and rounding.
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

# Be careful with effects due to things such as subtractive cancellation and
# adding large and small numbers together.
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))
print(math.fsum(nums))
