import matplotlib.pyplot as plt
import csv
import pandas as pd
file = open("c:/data/lotto_ball_nobonus.csv","r")
lotto_csv = csv.reader(file)
lotto_num = []
prime_num = []





def prime_number(number):
    if number!=1:
        for i in range(2,number):
            if number%i == 0:
                return False
    else:
        return False
    return True

for i in lotto_csv:
    lotto_num.append(i)
    
  

p_n = 0 
for i in lotto_num:
    for j in range(6):
        if prime_number(int(i[j])):
            p_n += 1

    prime_num.append(p_n)          
    p_n = 0
    

df = pd.DataFrame(prime_num,columns = ['prime_number'] ) 

a1 = df[(df['prime_number']==0)].count()
a2 = df[(df['prime_number']==1)].count()
a3 = df[(df['prime_number']==2)].count()
a4 = df[(df['prime_number']==3)].count()
a5 = df[(df['prime_number']==4)].count()
a6 = df[(df['prime_number']==5)].count()
a7 = df[(df['prime_number']==6)].count()


prime_num_pct = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7)]
s = pd.Series(prime_num_pct)
plt.figure(figsize = (7,5))
a = s.plot(kind = 'bar',width=0.4)
plt.title("당첨번호 소수 개수")
for i in a.patches:
     left,bottom,width,height=i.get_bbox().bounds
     a.annotate('%i'%height,(left+width/2,height+2),ha ='center',size=13)
#소수가 0개인 확률
persent = (int(p0)/int(df.count()))*100
