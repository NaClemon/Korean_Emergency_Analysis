# 성별 원형 그래프

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
data = pd.concat([data1, data2])

df1 = data['환자성별']
df1man = pd.DataFrame(df1[df1 == '남'])
df1wom = pd.DataFrame(df1[df1 == '여'])
df1str = pd.DataFrame(df1[df1 == '미상'])
strnum = df1str.count()
mannum = df1man.count()
womnum = df1wom.count()
nannum = df1.__len__() - df1.count()
group = [womnum, mannum, nannum]
plt.pie(group, labels=df1.unique()[:3], shadow=True,
        autopct='%1.2f%%',
        explode=(0.05, 0.05, 0.05))
plt.title('성별 구급 활동 발생 비율')
plt.show()