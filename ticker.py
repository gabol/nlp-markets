import pandas as pd

tickers = pd.read_csv('companylist.csv')

data = pd.concat([tickers['Symbol'], tickers['Name'], tickers['industry'], tickers['Sector'], tickers['MarketCap']], axis=1)
print(tickers.columns)
data.to_csv('symboldat.csv')