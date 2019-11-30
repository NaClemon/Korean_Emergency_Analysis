import folium
import pandas as pd

state_geo = 'Data/TL_SCCO_SIG.json'

state_age = 'Data/평균연령집계현황.csv'
state_data = pd.read_csv(state_age, sep=',', encoding='ANSI')
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x[4:])
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x.replace(' ', ''))
state_data = state_data[state_data['행정구역구분명'] == '시군']
print(state_data)

m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['행정구역명', '평균연령'],
 key_on='feature.properties.SIG_KOR_NM',
 fill_color='OrRd',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

m.save('Result/3-Gyeong-gi_Age.html')