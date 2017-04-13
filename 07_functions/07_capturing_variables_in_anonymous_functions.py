# Capture the values of certain variables at the time of definition.
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
# The value of x used in the lambda expression is a free variable that gets
# bound at runtime, not definition time. Thus, the value of x in the lambda
# expressions is whatever the value of the x variable happens to be at the
# time of execution.
print(a(10))
print(b(10))
x = 15
print(a(10))
x = 3
print(a(10))

# Include the value as a default value to capture a value at the point of
# definition and keep it.
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))

funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))

funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
