# Using a dictionary comprehension to extracting a subset of a dictionary.
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}

# Make a dictionary of all prices over 200.
p1 = {key: value for key, value in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks.
p2 = {key: value for key, value in prices.items() if key in tech_names}
print(p2)

# This can also be done by creating a sequence of tuples and passing them
# to the dict() function. The dictionary comprehension solution is a bit
# clearer and actually runs quite a bit faster.
p3 = dict((key, value) for key, value in prices.items() if value > 200)
print(p3)

# Sometimes there are multiple ways of accomplishing the same thing.
# However, this solution is almost 1.6 times slower than the p2 solution.
p4 = {key: prices[key] for key in prices.keys() & tech_names}
print(p4)
