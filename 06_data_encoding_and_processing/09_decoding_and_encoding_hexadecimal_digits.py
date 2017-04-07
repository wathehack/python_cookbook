import binascii
import base64


# To decode or encode a raw string of hex digits, use the binascii module.
# Encode as hex.
s = b'hello'
h = binascii.b2a_hex(s)
print(h)

# Decode back to bytes.
b = binascii.a2b_hex(h)
print(b)

# Similar functionality can also be found in the base64 module.
h = base64.b16encode(s)
print(h)
b = base64.b16decode(h)
print(b)
