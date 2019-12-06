# 구급활동 중 구급처종명 수

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

df = data[['구급처종명']].dropna(axis=0)

index = df['구급처종명'].unique()
datas = []
for kind in index:
    noEmbul = len(df[df['구급처종명'] == kind])
    if (kind == '기타'):
        noEmbul = noEmbul + len(data[['구급처종명']].isnull())
    datas.append(noEmbul)

for i in range(len(datas)):
    if (datas[i] < 1000):
        index = index[:i]
        datas = datas[:i]
        break

datas = np.array(datas)
temp = np.where(index == '기타')
index = np.delete(index, temp)
datas = np.delete(datas, temp)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(datas, autopct='%1.2f%%')
ax.legend(wedges, index,
          title="구급처종명",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
ax.set_title('구급처')
plt.show()