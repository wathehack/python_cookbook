from collections import defaultdict


# The built-in enumerate() function can iterate over a sequence, and keep
# track of which element of the sequence is currently being processed.
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# Pass in a start argument.
for idx, val in enumerate(my_list, 1):
    print(idx, val)

word_summary = defaultdict(list)
with open('somefile.txt', 'r') as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    # Create a list of words in current line.
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

# Unpacking tuples when applying enumerate() to a sequence of tuples.
data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)
try:
    for n, x, y in enumerate(data):
        print(n, x, y)
except ValueError as e:
    print(e)
