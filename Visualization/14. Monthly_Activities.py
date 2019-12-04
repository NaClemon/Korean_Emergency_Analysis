# 월별 신고 횟수

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import datetime
import seaborn as sns

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고년월일']]
data['신고년월일'] = pd.to_datetime(data['신고년월일'])

datas = []
sum = 0
for i in range(1, 13):
    day1 = datetime.datetime.strptime('2017-'+str(i), '%Y-%m')
    if (i != 12):
        day2 = datetime.datetime.strptime('2017-'+str(i + 1), '%Y-%m')
    else:
        day2 = datetime.datetime.strptime('2018-01', '%Y-%m')
    temp = len(data[(data['신고년월일'] >= day1) & (data['신고년월일'] < day2)])
    datas.append(temp)
    sum += temp

datau1 = pd.read_csv('Data/2018년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
datau2 = pd.read_csv('Data/2018년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
datau = pd.concat([datau1, datau2], sort=False)
datau = datau[datau['발생장소시도명'] == '경기도']
datau = datau[['신고년월일']]
datau['신고년월일'] = pd.to_datetime(datau['신고년월일'])

datasu = []
sum = 0
for i in range(1, 13):
    day1 = datetime.datetime.strptime('2018-'+str(i), '%Y-%m')
    if (i != 12):
        day2 = datetime.datetime.strptime('2018-'+str(i + 1), '%Y-%m')
    else:
        day2 = datetime.datetime.strptime('2019-01', '%Y-%m')
    temp = len(datau[(datau['신고년월일'] >= day1) & (datau['신고년월일'] < day2)])
    datasu.append(temp)
    sum += temp

index = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
a = np.array([datas], dtype=np.int64)
b = np.array([datasu], dtype=np.int64)
dataab = np.concatenate((a, b)).T
myData = pd.DataFrame(data=dataab,
                      index=index,
                      columns=['2017', '2018']).T

plt.figure(figsize=(10, 1))
sns.heatmap(myData, annot=True, fmt='d',
            linewidths=.5,
            cmap='OrRd')
plt.show()