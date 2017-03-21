import pickle


# Use the pickle module to serialize a Python object into a byte stream.
data = {'one': 1, 'two': 2, 'three': 3}
f = open('hello.bin', 'wb')
# To dump an object to a file.
pickle.dump(data, f)
# To dump an object to a string.
s = pickle.dumps(data)
print(s)

# To re-create an object from a byte stream, use either the pickle.load() or
# pickle.loads() functions.
f = open('hello.bin', 'rb')
# Restore from a file.
data = pickle.load(f)
print(data)
# Restore from a string.
data = pickle.loads(s)
print(data)
