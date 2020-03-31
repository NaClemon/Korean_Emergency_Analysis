import folium
import pandas as pd
import numpy as np

state_geo = 'Data/TL_SCCO_SIG.json'

state_age = 'Data/구급차및구급대원수현황.csv'
state_data = pd.read_csv(state_age, sep=',', encoding='ANSI')
state_data = state_data[state_data['집계년도'] == 2017]

index = []
for data in state_data['시군명']:
    if (data not in index):
        index.append(data)

data = []
for si in index:
    noEmbul = state_data[state_data['시군명'] == si]['구급차수(대)'].sum()
    data.append(noEmbul)

a = np.array([index])
b = np.array([data], dtype=np.int64)
datas = np.concatenate((a, b)).T

myData = pd.DataFrame(data=datas, index=range(len(index)), columns=['시군명', '구급차수(대)'])
myData = myData.astype({'구급차수(대)': 'int'})
print(myData)

m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=myData,
 columns=['시군명', '구급차수(대)'],
 key_on='feature.properties.SIG_KOR_NM',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('Result/4-Gyeong-gi_Embu.html')