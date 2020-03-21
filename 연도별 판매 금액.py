import matplotlib.pyplot as plt
import pandas as pd

lotto = pd.read_csv("c:/data/lotto.csv") 


lotto[pd.to_datetime(lotto['drwNoDate']).dt.year==2002].sum()
year_sell = lotto['totSellamnt'].groupby(pd.to_datetime(lotto['drwNoDate']).dt.year).sum()
year_sell = year_sell.drop(2002,0)
year_sell = year_sell.drop(2020,0)
plt.figure(figsize = (10,5))
year_sell.plot(kind = 'line')
plt.xlabel("year",fontsize=18)
plt.ylabel("TOTAL SELL",fontsize=15)
plt.xticks(year_sell.index,rotation = 70)
