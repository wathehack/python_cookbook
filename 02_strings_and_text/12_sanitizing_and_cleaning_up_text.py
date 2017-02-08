import unicodedata
import sys


# The problem of sanitizing and cleaning up text applies to a wide variety
# of problems involving text parsing and data handling.
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)

# Removing all combining characters.
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# A translation table that maps all Unicode decimal digit characters to their
# equivalent in ASCII.
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# Yet another technique for cleaning up text involves I/O decoding and
# encoding functions. The idea here is to first do some preliminary cleanup
# of the text, and then run it through a combination of encode() or decode()
# operations to strip or alter it.
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
