# parallel category 사용
# 관할구분

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly_express as px

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['관할구분', '출동소방서', '접수경로', '구급사고종별상위', '환자증상1']]

data = data.dropna(axis=0)

print(data)

fig = px.parallel_categories(data,
                             color_continuous_scale=px.colors.sequential.Inferno)
fig.show()