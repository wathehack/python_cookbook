import re


# Working with unicode characters in regular expressions.
# \d matches any unicode digit character.
num = re.compile('\d+')
# ASCII digits.
print(num.match('123'))
# Arabic digits.
print(num.match('\u0661\u0662\u0663'))

# Using the usual escape sequence for Unicode characters to include specific
# Unicode characters in patterns.
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')
