import unicodedata


# Making sure that all of the strings have the same underlying representation
# when working with Unicode strings.
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print(len(s1))
print(len(s2))

# Normalizing the text into a standard representation using the unicodedata
# module to fix problems of having multiple representations when comparing
# strings.
# The first argument to normalize() specifies how you want the string
# normalized. NFC means that characters should be fully composed (i.e., use a
# single code point if possible). NFD means that characters should be fully
# decomposed with the use of combining characters.
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1)
print(t2)
print(t1 == t2)
print(ascii(t1))

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3)
print(t4)
print(t3 == t4)
print(ascii(t3))

s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

# The combining() function tests a character to see if it is a combining
# character.
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))
