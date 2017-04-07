import sqlite3


# To interact with a relational database, use the sqlite3 module that comes
# with Python. If you are using a different database (e.g., MySql, Postgres,
# or ODBC), you'll have to install a third-party module to support it.
# However, the underlying programming interface will be virtually the same,
# if not identical.
db = sqlite3.connect('database.db')

# To do anything with the data, you next create a cursor. Once you have a
# cursor, you can start executing SQL queries.
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
c.executemany('insert into portfolio values (?, ?, ?)', stocks)
db.commit()

for row in db.execute('select * from portfolio'):
    print(row)

# Escape the parameters using ? to perform queries that accept user-supplied
# input parameters.
min_price = 100
for row in db.execute('select * from portfolio where price >= ?',
                      (min_price,)):
    print(row)
