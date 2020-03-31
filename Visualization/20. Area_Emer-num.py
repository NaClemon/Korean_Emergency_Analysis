# 면적과 구급시설

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly_express as px
import scipy.stats as stats

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data_area = pd.read_csv('Data/2017년 경기도 면적.csv', sep=',', encoding='ANSI')
data_area = data_area[data_area['시군별(2)'] != '소계']
data_area = data_area[['시군별(2)', '면적 (㎢)']]

data_embu = pd.read_csv('Data/구급차및구급대원수현황.csv', sep=',', encoding='ANSI')
data_embu = data_embu[data_embu['집계년도'] == 2017]
data_embu = data_embu[data_embu['구분명'] != '소방서']
data_embu = data_embu.groupby(['시군명']).size().reset_index(name='개수')

data_embu = data_embu.sort_values(["시군명"], ascending=[True])
data_area = data_area.sort_values(["시군별(2)"], ascending=[True]).reset_index(drop=True)

data = data_embu
data['면적'] = data_area['면적 (㎢)']
data['면적'] = pd.to_numeric(data['면적'])

print(data)
corr = data.corr(method='pearson')
cor = stats.pearsonr(data['개수'], data['면적'])
sns.heatmap(data=corr, annot=True, fmt='.3f', linewidths=.5, cmap='Blues')
plt.show()

