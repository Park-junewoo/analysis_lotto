import pandas as pd
from fbprophet import Prophet

df = pd.read_csv("c:/data/lotto.csv")


date = pd.to_datetime(df['drwNoDate'])
price = df['totSellamnt']


a = df['totSellamnt'].groupby([pd.to_datetime(df['drwNoDate']).dt.year,pd.to_datetime(df['drwNoDate']).dt.month]).sum()


df = pd.concat([date,price],axis = 1)
df.columns = ['ds','y']

m=Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=53,freq='W')
future.tail

forecast = m.predict(future)

m.plot(forecast)
