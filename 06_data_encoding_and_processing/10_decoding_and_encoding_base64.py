import base64


# To decode or encode binary data using Base64 encoding, use the base64
# module with b64encode() and b64decode() functions.
# Encode as Base64.
s = b'hello'
a = base64.b64encode(s)
print(a)

# Decode from Base64.
b = base64.b64decode(a)
print(b)
