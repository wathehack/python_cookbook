def add(x: int, y: int) -> int:
    '''
    Function argument annotations can be a useful way to give programmers
    hints about how a function is supposed to be used. The Python interpreter
    does not attach any semantic meaning to the attached annotations. They
    are not type checks, nor do they make Python behave any differently than
    it did before. However, they might give useful hints to others reading the
    source code about what you had in mind.
    '''
    return x + y

help(add)

# Function annotations are merely stored in a function's __annotations__
# attribute.
print(add.__annotations__)
