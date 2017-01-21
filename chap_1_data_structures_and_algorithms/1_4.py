import heapq


# Making a list of the largest or smallest N items in a collection using the
# heapq module.
def find_largest(n, nums):
    return heapq.nlargest(n, nums)


def find_smallest(n, nums):
    return heapq.nsmallest(n, nums)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(find_largest(2, nums))
print(find_smallest(2, nums))

# Both nlargest() and nsmallest() also accept a key parameter that allows them
# to be used with more complicated data structures.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)

# The most important feature of a heap is that heap[0] is always the smallest
# item. Moreover, subsequent items can be easily found using the
# heapq.heappop() method, which pops off the first item and replaces it with
# the next smallest item (an operation that requires O(log N) operations where
# N is the size of the heap).
heap = list(nums)
heapq.heapify(heap)
print(heap)
# Prints -4.
print(heapq.heappop(heap))
# Prints 1.
print(heapq.heappop(heap))

# If you are simply trying to find the single smallest or largest item (N=1),
# it is faster to use min() and max().
print('Max:', max(nums))
print('Min:', min(nums))

# If N is about the same size as the collection itself, it is usually faster
# to sort it first and take a slice.
print('Largest 8 items:', sorted(nums)[-8:])
print('Smallest 8 items:', sorted(nums)[:8])
