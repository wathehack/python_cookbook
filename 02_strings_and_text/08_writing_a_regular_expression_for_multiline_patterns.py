import re


# Matching a block of text span multiple lines using a regular expression.
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */
'''

comment = re.compile(r'/\*(.*?)\*/')
print(comment.findall(text1))
print(comment.findall(text2))

# In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines a
# group for the purposes of matching, but that group is not captured
# separately or numbered).
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# The re.compile() function accepts a flag, re.DOTALL, which makes the . in
# a regular expression match all characters, including newlines.
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
