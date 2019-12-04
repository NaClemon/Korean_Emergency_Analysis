# 구급활동 중 환자증상 수

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
from PIL import Image
import numpy as np
from wordcloud import WordCloud

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

df = data[['환자증상1']].dropna(axis=0)
index = df['환자증상1'].unique()

datas = []
for kind in index:
    noEmbul = len(df[df['환자증상1'] == kind])
    if (kind == '기타'):
        noEmbul = noEmbul + len(data[['환자증상1']].isnull())
    datas.append(noEmbul)

freq = {}

for i in range(len(index)):
    freq[index[i]] = datas[i]
mask = np.array(Image.open('Image/Emergency.png'))
wc = WordCloud(
    font_path=font_location,
    width=800,
    height=800,
    background_color='white',
    mask=mask
)
wc = wc.generate_from_frequencies(freq)

fig = plt.figure(figsize=(5, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
