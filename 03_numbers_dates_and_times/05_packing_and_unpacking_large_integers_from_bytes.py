import struct


# To interpret the bytes as an integer, use the int.from_bytes() method,
# specifying the byte order.
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

# To convert a large integer value back into a byte string, use the
# int.to_bytes() method, specifying the number of bytes and the byte order.
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# Unpacking values using the struct module.
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo

# The specification of the byte order (little or big) just indicates whether
# the bytes that make up the integer value are listed from the least to most
# significant or the other way around.
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

# Using the int.bit_length() method to determine how many bits are required
# to store a value if needed.
x = 523 ** 23
print(x)
try:
    print(x.to_bytes(16, 'little'))
except Exception as e:
    print(e)
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
