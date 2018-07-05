import pandas_datareader.data as web
import datetime
start = datetime.datetime(2013, 1, 1)
end = datetime.date.today()
f = web.DataReader('PFE', 'iex', start, end)
x = f.to_html('stock_nyse.html')
# a = f.ix['2017-01-04']
print(f)