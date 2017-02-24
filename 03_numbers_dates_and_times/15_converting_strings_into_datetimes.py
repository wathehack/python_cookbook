from datetime import datetime


# Python's standard datetime module converts temporal data in string format
# into datetime objects.
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(y)
print(z)
print(diff)

# Format a nice, human-readable date.
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)
