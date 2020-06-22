from urllib.request import urlopen
from bs4 import BeautifulSoup


# 습도 - https://www.weather.go.kr/weather/observation/currentweather.jsp?tm=2020.06.19.01:00&type=t13&mode=0&reg=100&auto_man=m&stn=129
# 이슬점 - https://www.weather.go.kr/weather/observation/currentweather.jsp?tm=2020.06.19.01:00&type=t12&mode=0&reg=100&auto_man=m&stn=129
import datetime

date1 = '2016-05-01'
date2 = '2019-04-18'
start = datetime.datetime.strptime(date1, '%Y-%m-%d')
end = datetime.datetime.strptime(date2, '%Y-%m-%d')
step = datetime.timedelta(days=30)

tmp = {}

while start <= end:
    print (str(start.date()).replace("-" , "."))
    
    basic_path = "https://www.weather.go.kr/weather/observation/currentweather.jsp?type=t13&mode=2&stn=129&reg=101&auto_man=m&tm="
    basic_path2 = ".01:00&dtm=0"
    date = str(start.date()).replace("-" , ".")
    url = basic_path+date+ basic_path2
    html = urlopen(url)
    source = html.read()
    #print(html)
    soup = BeautifulSoup(source, "html5lib")
    
    #print(soup)
    tr=soup.find_all("tr")
    #print(tr)
    html.close()
    
    # =============================================================================
    # tr[1].find("a")
    # tr[1].a.attrs
    # tr[1].a.string
    # tr[1].find_all("td")[1:]
    # =============================================================================
       
    for i in range(1 ,32):#len(tr)):
        #print(tr[i].a.string)
        tmp2 = []
        for j in tr[i].find_all("td")[1:]:
            #print(j.string)
            tmp2.append(j.string)
        tmp[str(start.year)+"."+tr[i].a.string] = tmp2
    start += step
    
print(tmp.keys())

answer={}
#for i in tmp.keys():
for i in tmp.keys():    
    print(i)
    for j in range(0,8):
        answer[(datetime.datetime.strptime(i, '%Y.%m.%d') + datetime.timedelta(hours= (j+1)*3)).strftime('%Y-%m-%d %H')] = tmp[i][j]
        #print((datetime.datetime.strptime(i, '%Y.%m.%d') + datetime.timedelta(hours= (j+1)*3)).strftime('%Y-%m-%d %H'))

type(answer)
answer['2016-05-02 00']
'''
import pandas as pd
df = pd.DataFrame(answer.values() , index = answer.keys() , columns = ["dew_point"])
df

df.to_csv("dewpoint.csv")

print(df)


df2 = pd.read_csv("dewpoint.csv")
type(df2)
df2 = df2.set_index('Unnamed: 0')
df2
'''