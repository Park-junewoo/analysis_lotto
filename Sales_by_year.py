import matplotlib.pyplot as plt
import pandas as pd

lotto = pd.read_csv("c:/data/lotto.csv") 


lotto[pd.to_datetime(lotto['drwNoDate']).dt.year==2002].sum()
year_sell = lotto['totSellamnt'].groupby(pd.to_datetime(lotto['drwNoDate']).dt.year).sum()
year_sell = year_sell.drop(2002,0)
year_sell = year_sell.drop(2020,0)
plt.figure(figsize = (10,5))
year_sell.plot(kind = 'line')
plt.title("연도별 판매 금액",size = 20)
plt.xlabel("year",fontsize=18)
plt.ylabel("TOTAL SELL",fontsize=15)
plt.xticks(year_sell.index,rotation = 70)
plt.text(2003.5 ,year_sell.max(),s = '최대 판대액 2019년: '+str(format(int(year_sell.max()),','))+'원',fontsize = 11)
plt.text(2003.5 ,year_sell.max()-(10**11),s = '최저 판대액 2007년: '+str(format(int(year_sell.min()),','))+'원',fontsize = 11)
