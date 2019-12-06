# 연령별 발생 비율
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

df1 = data['환자연령']
dtemp = pd.DataFrame(df1)
dtemp['환자연령'] = np.where(dtemp['환자연령'], np.floor(dtemp['환자연령']/10), dtemp['환자연령'])
dtemp['환자연령'] = dtemp['환자연령'].fillna(-1).astype(np.int)

ages = []
for age in dtemp['환자연령'].unique():
    if (age > -1 and age < 12):
        ages.append(age)

for i in range(1, len(ages)):
    key = ages[i]
    j = i - 1
    while (j >= 0 and ages[j] > key):
        ages[j + 1] = ages[j]
        j = j - 1
    ages[j + 1] = key

data = []
for i in ages:
    noAccident = int(pd.DataFrame(dtemp[dtemp['환자연령'] == i]).count())
    data.append(noAccident)
    plt.text(i, noAccident, '%d명'%noAccident, fontsize=7, color='#ff6600',
             horizontalalignment='center', verticalalignment='bottom')

plt.bar(np.arange(len(ages)), data)
plt.ylabel('횟수')
plt.xlabel('연령대')
plt.xticks(np.arange(len(ages)), ages)
plt.show()