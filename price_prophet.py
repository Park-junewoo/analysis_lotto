import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt
plt.style.use('bmh')

df = pd.read_csv("c:/data/lotto.csv")


date = pd.to_datetime(df['drwNoDate'])
price = df['totSellamnt']


a = df['totSellamnt'].groupby([pd.to_datetime(df['drwNoDate']).dt.year,pd.to_datetime(df['drwNoDate']).dt.month]).sum()


df = pd.concat([date,price],axis = 1)
df.columns = ['ds','y']

one_year_df = df[df['ds']>'2019-03-20']
five_year_df = df[df['ds']>'2015-03-20']
ten_year_df = df[df['ds']>'2010-03-20']


#all
m=Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=53,freq='W')
future.tail

forecast = m.predict(future)

m.plot(forecast)

'''
#ten year ago
m=Prophet()
m.fit(ten_year_df)

future = m.make_future_dataframe(periods=52,freq='W')
future.tail

forecast = m.predict(future)

m.plot(forecast)

#five year ago
m=Prophet()
m.fit(five_year_df)

future = m.make_future_dataframe(periods=52,freq='W')
future.tail

forecast = m.predict(future)

m.plot(forecast)

#one year ago
m=Prophet()
m.fit(one_year_df)

future = m.make_future_dataframe(periods=52,freq='W')
future.tail

forecast = m.predict(future)

m.plot(forecast)
'''
