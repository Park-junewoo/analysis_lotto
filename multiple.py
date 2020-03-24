import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time
from itertools import combinations
start = time.time()
file = open("c:/data/lotto_ball_nobonus.csv","r")
lotto_csv = csv.reader(file)
lotto_num = []
three_times = 0
four_times = 0
five_times = 0
seven_times = 0
round_dict = {}
for i in lotto_csv:
    lotto_num.append(i)


#40과 같은 수는 4배수와 5배수의 걸치기 때문에 다중 for문을 적용
cn = 1
for i in lotto_num:
    for j in range(6):
        if int(i[j])%3==0:
            three_times+=1
            
    for j in range(6):
        if int(i[j])%4==0:
            four_times+=1

    for j in range(6):
        if int(i[j])%5==0:
            five_times+=1

    for j in range(6):
        if int(i[j])%7==0:
            seven_times+=1

    round_dict[cn] = [three_times,four_times,five_times,seven_times]
    cn+=1
    three_times = 0
    four_times = 0
    five_times = 0
    seven_times = 0

a = pd.DataFrame(round_dict)

a = a.T
#columns = {'3의배수','4의배수','5의배수','7의배수'}

a.rename(columns = {0:'3times',1:'4times',2:'5times',3:'7times'}, inplace = True) 

#모든 배수가 0이 아닌 경우
a1 = a[(a['3times']>0)&(a['4times']>0)&(a['5times']>0)&(a['7times']>0)] 

#한 배수만 없는 경우
a2 = a[(a['3times']==0)&(a['4times']>0)&(a['5times']>0)&(a['7times']>0)] 
a3 = a[(a['3times']>0)&(a['4times']==0)&(a['5times']>0)&(a['7times']>0)] 
a4 = a[(a['3times']>0)&(a['4times']>0)&(a['5times']==0)&(a['7times']>0)] 
a5 = a[(a['3times']>0)&(a['4times']>0)&(a['5times']>0)&(a['7times']==0)] 

x = pd.concat([a2,a3,a4,a5]).sort_index()

b = pd.concat([a1,a2,a3,a4,a5])

b = b.sort_index()
len(b)/len(a)*100
#b = a[(a['3times']==0)]  
#len(b)/len(a)*100


three_times = 0
four_times = 0
five_times = 0
seven_times = 0
round_dict = {}
a = []
for i in range(1,46,1):
    a.append('{}'.format(i))
lotto = list(combinations(a,6))
cn = 1
for i in lotto:
    for j in range(6):
        if int(i[j])%3==0:
            three_times+=1
            
    for j in range(6):
        if int(i[j])%4==0:
            four_times+=1

    for j in range(6):
        if int(i[j])%5==0:
            five_times+=1

    for j in range(6):
        if int(i[j])%7==0:
            seven_times+=1

    round_dict[cn] = [three_times,four_times,five_times,seven_times]
    cn+=1
    three_times = 0
    four_times = 0
    five_times = 0
    seven_times = 0
    
all_case = pd.DataFrame(round_dict)
print("작업시간 :", time.time() - start,'초')
        

