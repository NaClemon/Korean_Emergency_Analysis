# 구급활동 중 의식상태 원형 차트

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

df = data[['의식상태']].dropna(axis=0)

index = df['의식상태'].unique()
print(index)
datas = []
for kind in index:
    noEmbul = len(df[df['의식상태'] == kind])
    datas.append(noEmbul)

print(datas)

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
wedges, texts, autotexts = ax.pie(datas, autopct='%1.2f%%')
ax.legend(wedges, index,
          title="의식상태",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
ax.set_title('의식상태')
plt.show()