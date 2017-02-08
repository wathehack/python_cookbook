import re


# Using regular expressions to find the shortest possible match.
# The * operator in a regular expression is greedy, so matching is based on
# finding the longest possible match.
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# Adding the ? modifier after the * operator in the pattern makes the matching
# nongreedy, and produces the shortest match instead.
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
