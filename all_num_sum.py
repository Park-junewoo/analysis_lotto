import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import time
start = time.time()
file = open("c:/data/lotto_ball_nobonus.csv","r")
lotto_csv = csv.reader(file)
lotto_num = []
lotto_sum = []


for i in lotto_csv:
    lotto_num.append(i)
    
for i in lotto_num:
    i = list(map(int,i))#list 안에 값을 str에서 int로 형변환
    lotto_sum.append(sum(i))


a = pd.DataFrame(lotto_sum,columns = ["lotto_sum"],)

bins = np.arange(0,261,20)
b = pd.cut(lotto_sum,bins)  #동일한 길이로 나누기 cut

c = a.lotto_sum.groupby(b) #cut 기준으로 lotto_sum 열 groupby

d = c.agg(['count'])  #개수 출력

#d['persentage']= [1,2,3,5,6,7,8,9,10,11,12,13,14]
persentage = []
for i in c:
    persentage.append(i[1].count()/900*100)

d["persentage"] = persentage


print(d)

#히스토그램
plt.hist(lotto_sum ,bins = np.arange(0,261,20))
#막대그래프
d['count'].plot(kind='bar')


print("작업시간 :", time.time() - start)
