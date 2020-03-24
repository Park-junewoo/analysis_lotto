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


a = pd.DataFrame(lotto_sum,columns = ["lotto_sum"])

bins = np.arange(0,261,20)
b = pd.cut(lotto_sum,bins)  #동일한 길이로 나누기 cut

c = a.lotto_sum.groupby(b) #cut 기준으로 lotto_sum 열 groupby

sum_902 = c.agg(['count'])  #개수 출력

#d['persentage']= [1,2,3,5,6,7,8,9,10,11,12,13,14]
pct = []
for i in c:
    pct.append(round((i[1].count()/len(lotto_sum)*100),2))

sum_902["pct"] = pct


print(sum_902)

#히스토그램
plt.hist(lotto_sum ,bins = np.arange(0,261,20))
#막대그래프
sum_902['count'].plot(kind='bar')
plt.xticks(rotation = 50)



#8145060가지 조합 모든 경우의수
a = []
for i in range(1,46,1):
    a.append('{}'.format(i))
lotto = list(combinations(a,6))

lotto_sum = []
for i in lotto:
    i = list(map(int,i)) #list 안에 값을 str에서 int로 형변환
    lotto_sum.append(sum(i))
    
    
a1 = pd.DataFrame(lotto_sum,columns = ["lotto_sum"])


bins1 = np.arange(0,261,20)
b1 = pd.cut(lotto_sum,bins)  #동일한 길이로 나누기 cut

c1 = a1.lotto_sum.groupby(b1) #cut 기준으로 lotto_sum 열 groupby

all = c1.agg(['count'])  #개수 출력

#d['persentage']= [1,2,3,5,6,7,8,9,10,11,12,13,14]
pct = []
for i in c1:
    pct.append(round(i[1].count()/len(lotto_sum)*100,2))

all["pct"] = pct

print(all)
all['pct'].plot(kind='bar')
plt.xticks(rotation = 50)

df = pd.concat([sum_902['pct'],all['pct']],axis = 1)
df.columns = ['sum_902_pct','all_pct']
df.plot(kind = 'bar')
plt.legend(labels = ['902회차','모든 경우의 수'])
plt.xticks(rotation =70)
plt.title("번호의 합")
print("작업시간 :", time.time() - start)
