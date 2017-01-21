from collections import Counter


# Determine the most frequently occurring items in the sequence.
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts.update(morewords)
print(word_counts)

a = Counter(words)
print(a)

b = Counter(morewords)
print(b)

c = a + b
print(c)

d = a - b
print(d)
