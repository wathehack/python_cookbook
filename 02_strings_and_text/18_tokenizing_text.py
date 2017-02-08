import re
from collections import namedtuple


# Tokenizing text.
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
for m in iter(scanner.match, None):
    print(m.lastgroup, m.group())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'bar = 23'):
    print(tok)

# Defining more generator functions or use a generator expression to filter
# out all whitespace tokens.
tokens = (tok for tok in generate_tokens(master_pat, 'whitespace = 0')
          if tok.type != 'WS')
for tok in tokens:
    print(tok)

# The order of tokens in the master regular expression matters. When matching,
# re tries to match pattens in the order specified. If a pattern happens to
# be a substring of a longer pattern, make sure the longer pattern goes first.
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
correct_pat = re.compile('|'.join([LE, LT, EQ]))
incorrect_pat = re.compile('|'.join([LT, LE, EQ]))
for tok in generate_tokens(correct_pat, '<='):
    print(tok)
for tok in generate_tokens(incorrect_pat, '<='):
    print(tok)
