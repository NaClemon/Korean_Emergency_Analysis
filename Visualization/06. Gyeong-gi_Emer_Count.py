# 지역별 긴급구조횟수

import numpy as np
import pandas as pd
import folium
import re

state_geo = 'Data/TL_SCCO_SIG.json'

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[data['긴급구조시'] == '경기도']
df = data[['긴급구조구']]
df = df.dropna(axis=0)

df['긴급구조구'] = df.긴급구조구.apply(lambda x: x[:4])
df['긴급구조구'] = df.긴급구조구.apply(lambda x: x.replace(' ', ''))

index = []
for data in df['긴급구조구']:
    if (data not in index):
        index.append(data)

datas = []
for si in index:
    noEmbul = len(df[df['긴급구조구'] == si])
    datas.append(noEmbul)

index = index[:len(index) - 1]
datas = datas[:len(datas) - 1]

a = np.array([index])
b = np.array([datas], dtype=np.int64)
dataComb = np.concatenate((a, b)).T

myData = pd.DataFrame(data=dataComb, index=range(len(index)), columns=['긴급구조구', '긴급구조횟수'])
myData = myData.astype({'긴급구조횟수': 'int'})
print(myData)

m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=myData,
 columns=['긴급구조구', '긴급구조횟수'],
 key_on='feature.properties.SIG_KOR_NM',
 fill_color='YlOrRd',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('Result/7-Gyeong-gi_Emer_Count.html')