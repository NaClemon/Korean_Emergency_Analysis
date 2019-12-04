# 연령별
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data = pd.read_csv('Data/주민등록인구집계현황.csv', sep=',', encoding='ANSI')
df = data.loc[:0, '0~9세':'100세 이상']
print(df)

ages = ['0대', '10대', '20대', '30대', '40대', '50대', '60대',
        '70대', '80대', '90대', '100대']

datas = []
k = 0
for i in df:
    temp = df[i].sum()
    datas.append(temp)

print(datas)

plt.bar(np.arange(len(ages)), datas)
plt.ylabel('횟수')
plt.xlabel('연령대')
plt.xticks(np.arange(len(ages)), ages)
plt.show()