import pandas


# For any kind of data analysis involving statistics, time series, and other
# related techniques, you should look at the Pandas library.
# Read a CSV file.
stocks = pandas.read_csv('stocks_1.csv')

# Investigate range of values for a certain field.
print(stocks['Symbol'].unique())

# Filter the data.
high_price = stocks[stocks['Price'] > 60]
print(len(high_price))

# Group by date.
dates = stocks.groupby('Date')
print(len(dates))

# Determine counts on each day.
date_counts = dates.size()
print(date_counts[0])

# Sort the counts.
date_counts.sort_values(inplace=True)
print(date_counts[0])
