import matplotlib.pyplot as plt
import pandas as pd
import csv
from itertools import combinations
file = open("c:/data/lotto_ball_nobonus.csv","r")
lotto_csv = csv.reader(file)
next(lotto_csv)
lotto_num = []
even_odd = []
even_odd_percent = []
a = []
for i in range(1,46,1):
    a.append('{}'.format(i))

lotto = list(combinations(a,6))
 
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
even_odd_percent = s.value_counts(normalize=True) #normalize옵션으로 비율 구하기
even_odd_percent = even_odd_percent.sort_index()

print(even_odd_percent*100)
 
a = plt.subplot()
a.set_xticks([0,1,2,3,4,5,6])
a.set_xticklabels(['0:6','1:5','2:4','3:3','4:2','5:1','6:0'])
plt.xlabel('EVEN:ODD')
plt.ylabel('percent')
plt.bar(range(len(even_odd_percent)),even_odd_percent)

'''
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
even_odd_percent1 = s1.value_counts(normalize=True) #normalize옵션으로 비율 구하기
even_odd_percent1 = even_odd_percent1.sort_index()

print(even_odd_percent1*100)
 
df = pd.concat([even_odd_percent,even_odd_percent1],axis = 1)



df[[0,1]].plot(kind = 'bar')
plt.legend(labels = ['902회차','모든 경우의 수'])
plt.xticks(rotation =0)

'''