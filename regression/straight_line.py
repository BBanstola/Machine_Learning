import pandas as pd
import quandl
import math

# use a API key for getting the dataset without much hassle [You'll get one once you sign in at quandl]

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

df['HC_%'] = (df ['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

df['%_change'] = (df ['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HC_%','%_change','Adj. Volume']]

# print(df.head())

forecast_col = 'Adj. Close'

df. fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

print(df.head)
