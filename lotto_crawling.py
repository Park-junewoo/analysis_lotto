from urllib.request import urlopen 
import pandas as pd 
import json


for i in range(1,1000,1): 
    url="http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo="+str(i) 
    result_data = urlopen(url) 
    result = result_data.read() 
    lotto = json.loads(result) 
    lotto_num = ({str(lotto["drwNo"])+','+
                  str(lotto["drwNoDate"])+','+
                  str(lotto["totSellamnt"])+','+
                  str(lotto["firstAccumamnt"])+','+
                  str(lotto["firstPrzwnerCo"])+','+
                  str(lotto["firstWinamnt"])+','+
                  str(lotto["drwtNo1"])+','+
                  str(lotto["drwtNo2"])+','+
                  str(lotto["drwtNo3"])+','+
                  str(lotto["drwtNo4"])+','+
                  str(lotto["drwtNo5"])+','+
                  str(lotto["drwtNo6"])+','+
                  str(lotto["bnusNo"])}) 
    print(lotto_num) 
    df = pd.DataFrame(lotto_num) 
    df.to_csv("c:/data/lotto_csv.csv",header=False , mode='a')
    
    
    
    