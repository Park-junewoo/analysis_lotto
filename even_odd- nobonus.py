import matplotlib.pyplot as plt
import pandas as pd
import csv
from itertools import combinations
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc
from matplotlib import style
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
file = open("c:/data/lotto_ball_nobonus.csv","r")
lotto_csv = csv.reader(file)
next(lotto_csv)
lotto_num = []
even_odd = []
even_odd_percent = []

 
#홀짝 분석 
#당첨번호에서 홀과 짝의 비율을 말한다
 
for i in lotto_csv:
    lotto_num.append(i)
    
  
 
odd = 0 
even = 0
for i in lotto_num:
    for j in range(6):
        if int(i[j])%2 == 0:
                even += 1
        else:
                odd += 1
    even_odd.append([even,odd])          
    odd = 0 
    even = 0


    

s = pd.Series(even_odd) 
round_902_pct = s.value_counts(normalize=True) #normalize옵션으로 비율 구하기
round_902_pct = round_902_pct.sort_index()

 

#8145060가지 조합 모든 경우의수 
a = []
for i in range(1,46,1):
    a.append('{}'.format(i))
lotto = list(combinations(a,6))

even_odd = []
for i in lotto:
    for j in range(6):
        if int(i[j])%2 == 0:
                even += 1
        else:
                odd += 1
    even_odd.append([even,odd])          
    odd = 0 
    even = 0
    
    
s1 = pd.Series(even_odd) 
all_case = s1.value_counts(normalize=True) #normalize옵션으로 비율 구하기
all_case = all_case.sort_index()

print(all_case*100)
 
df = pd.concat([round_902_pct,all_case],axis = 1)

round_902_pct.iloc[2:5].sum()*100
all_case.iloc[2:5].sum()*100


df[[0,1]].plot(kind = 'bar')
plt.legend(labels = ['902회차','모든 경우의 수'])
plt.xticks(rotation =0)
