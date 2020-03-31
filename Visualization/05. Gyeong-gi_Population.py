# 지역별 총 인구수

import folium
import pandas as pd
import numpy as np

state_geo = 'Data/TL_SCCO_SIG.json'

state_age = 'Data/주민등록인구집계현황.csv'
state_data = pd.read_csv(state_age, sep=',', encoding='ANSI')
state_data = state_data[['행정구역구분명', '행정구역명', '총 인구수']]
state_data = state_data[state_data['행정구역구분명'] == '시군']
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x[4:])
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x.replace(' ', ''))
print(state_data)

m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['행정구역명', '총 인구수'],
 key_on='feature.properties.SIG_KOR_NM',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('Result/6-Gyeong-gi_Population.html')