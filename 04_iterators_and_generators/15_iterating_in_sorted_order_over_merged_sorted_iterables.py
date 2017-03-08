import heapq


# The heapq.merge() function iterates over a collection of sorted sequences.
# heapq.merge() requires that all of the input sequences already be sorted.
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)
