import csv
import re
from collections import namedtuple


# To read or write data encoded as a CSV file, use the csv library.
with open('stocks_1.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Row will be a tuple. To access certain fields, use indexing, such as
        # row[0] (Symbol) and row[4] (Change).
        print(row)

# To use the column headers such as row.Symbol and row.Change instead of
# indices, use namedtuple module. This only works if the column headers are
# valid Python identifiers.
with open('stocks_1.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    for r in f_csv:
        row = Row(*r)
        print(row)

# To access the elements of each row using row['Symbol'] or row['Change'],
# read the data as a sequence of dictionaries.
with open('stocks_1.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

# To write CSV data, use the csv module to create a writer object.
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
        ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
        ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
        ]
with open('stocks_2.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# If the data is a sequence of dictionaries, use csv.DictWriter.
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
        ]
with open('stocks_3.csv', 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# A CSV file could have a header line containing nonvalid identifier
# characters. It will cause the creation of a namedtuple to fail with a
# ValueError exception. To work around this, scrub the headers first.
with open('location.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row)

# Performing extra type conversions on CSV data.
col_types = [str, float, str, str, float, int]
with open('stocks_1.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items.
        row = tuple(convert(value) for convert, value in zip(col_types, row))

# Converting selected fields of dictionaries.
print('Reading as dicts with type conversion')
field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]
with open('stocks_1.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)
