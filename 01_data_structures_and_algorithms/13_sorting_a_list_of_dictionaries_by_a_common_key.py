from operator import itemgetter


# Sorting the entries of a list of dictionaries according to one or more of
# the dictionary values.
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() function can also accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# The functionality of itemgetter() is sometimes replaced by lambda
# expressions. However, the solution involving itemgetter() typically runs
# a bit faster.
rows_by_lname = sorted(rows, key=lambda r: r['lname'])
print(rows_by_lname)

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
