from statistics import mean


# Unpacking elements from iterables of arbitrary length.
def drop_first_last(grades):
    first, *middle, last = grades
    return mean(middle)

print(drop_first_last([77, 84, 81, 69, 98, 64, 87]))

# The phone_numbers variable will always be a list, regardless of how many
# phone numbers are unpacked.
user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(phone_numbers)

sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
print(trailing_avg, current_qtr)


# The star syntax can be especially useful when iterating over a sequence of
# tuples of varying length.
def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Star unpacking can also be useful when combined with certain kinds of string
# processing operations, such as splitting.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(fields)
print(*fields)

# Using a common throwaway variable name, such as _ or ign (ignored).
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)


# Recursive algorithm in functional programming.
def sum(nums):
    head, *tail = nums
    return head + sum(tail) if tail else head

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
