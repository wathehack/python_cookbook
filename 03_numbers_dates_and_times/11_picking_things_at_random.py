import random
import ssl


# The random module has various functions for random numbers and picking
# random items.
# To pick a random item out of a sequence, use random.choice().
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))

# To take a sampling of N items where selected items are removed from further
# consideration, use random.sample().
print(random.sample(values, 2))

# To shuffle items in a sequence in place, use random.shuffle().
random.shuffle(values)
print(values)

# To produce random integers, use random.randint().
print(random.randint(0, 10))

# To produce uniform floating-point values in the range 0 to 1, use
# random.random().
print(random.random())

# To get N random-bits expressed as an integer, use random.getrandbits().
print(random.getrandbits(200))

# The random module computes random numbers using the Mersenne Twister
# algorithm. This is a deterministic algorithm, but you can alter the initial
# seed by using the random.seed() function.
random.seed()
random.seed(12345)
random.seed(b'bytedata')

# Functions in random() should not be used in programs related to cryptography.
# If you need such functionality, consider using functions in the ssl module
# instead.
ssl.RAND_bytes(12345)
