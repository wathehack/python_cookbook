from itertools import compress


# Using a list comprehension to filter sequence data.
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

# One potential downside of using a list comprehension is that it might
# produce a large result if the original input is large. If this is a
# concern, you can use generator expressions to produce the filtered
# values iteratively.
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)


# For the filtering process involves exception handling or some other
# complicated detail, put the filtering code into its own function and use
# the built-in filter() function.
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

# Another notable filtering tool is itertools.compress(), which takes an
# iterable and an accompanying Boolean selector sequence as input. As output,
# it gives you all of the items in the iterable where the corresponding
# element in the selector is True.
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
