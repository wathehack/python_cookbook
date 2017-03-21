# Using the sep and end keyword arguments to print() to change the separator
# character or line ending.
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep='---')
print('ACME', 50, 91.5, sep='---', end='#####\n')

# Suppress the output of newlines in output.
for i in range(5):
    print(i)
for i in range(5):
    print(i, end=' ')
print('\n')

# Using str.join() can also change the separator character or line ending.
# However, str.join() only works with strings.
row = ('ACME', 50, 91.5)
try:
    print('***'.join(row))
except Exception as e:
    print(e)
print('***'.join(str(x) for x in row))
print(*row, sep='***')
