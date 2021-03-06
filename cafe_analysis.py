import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import folium
from folium import plugins
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore', 'This pattern has match groups')
warnings.filterwarnings('ignore', 'The iterable function was deprecated in Matplotlib')

# 데이터 로딩
data=pd.read_csv('cafe_data.csv', encoding='cp949')
#print(data.columns)
#print(data.head(5))

# 한글 인식을 위한 작업
mpl.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 10
plt.rcParams["figure.figsize"] = (14,4)

data[['위도', '경도']].describe(include=np.number)
data['위도']=data['위도'].astype(float)
data['경도']=data['경도'].astype(float)


# 그래프상에서 카페 위치 출력
sns.relplot(data=data, x="경도", y="위도", hue="동", palette=sns.color_palette("colorblind", 19))
plt.title('위도, 경도별 카페 분포',fontsize=20)
plt.show()


# 위도 경도 정보 저장
map_alt=[] #위도 값가 들어갈 list
map_long=[] #경도 값이 들어갈 list
for i in range(len(data)):
    map_alt.append(data['위도'].iloc[i])
    map_long.append(data['경도'].iloc[i])


# popup 창에 가격을 띄우려고 했더니 숫자형은 불가능하다고 해서 int형인 아메리카노 가격을 string으로 바꿈
# 아메리카노 가격을 제대로 인식하지 못해 데이터 index값을 저장하는 리스트를 만들어서 casting과 동시에 index 정보도 저장함.
string_price=[]
index_list = []
for a in range(len(data)):
    index_list.append(a)
    temp=str(data['아메리카노'].iloc[i])
    string_price.append((temp))


# 동 별로 다른 색으로 카페 위치 지도에 표시
map_dong=folium.Map(location=[data['위도'].iloc[0], data['경도'].iloc[0]], zoom_start=13)
for index in range(len(index_list)):
    i=index_list[index]
    if(data['동'].iloc[i]==1):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FF0000', fill_color='#FF0000').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==2):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#F29661', fill_color='#F29661').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==3):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#980000', fill_color='#980000').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==4):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FFBB00', fill_color='#FFBB00').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==5):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#E5D85C', fill_color='#E5D85C').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==6):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#997000', fill_color='#997000').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==7):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#1F3456', fill_color='#1F3456').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==8):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#ABF200', fill_color='#ABF200').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==9):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#86E57F', fill_color='#86E57F').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==10):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#6B9900', fill_color='#6B9900').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==11):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#00D8FF', fill_color='#00D8FF').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==12):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#6799FF', fill_color='#6799FF').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==13):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#008299', fill_color='#008299').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==14):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#0100FF', fill_color='#0100FF').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==15):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#A566FF', fill_color='#A566FF').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==16):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#D26C9F', fill_color='#D26C9F').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==17):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#FF00DD', fill_color='#FF00DD').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==18):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#F361A6', fill_color='#F361A6').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)
    if(data['동'].iloc[i]==19):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7,popup=i, color='#990085', fill_color='#990085').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong)

map_dong.save('map_dong.html', encoding='utf-8')


# 아메리카노 가격에 따른 지도 위에 마커 표시
# 가격이 비쌀 수록 진한 색으로 표기
map_dong_price=folium.Map(location=[data['위도'].iloc[0], data['경도'].iloc[0]], zoom_start=13)
for index in range(len(index_list)):
    i=index_list[index]
    if(data['가격'].iloc[i]==1):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#FFA46C', fill_color='#FFA46C').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==2):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#CF6E36', fill_color='#CF6E36').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==3):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#993800', fill_color='#993800').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==4):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#630200', fill_color='#630200').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==5):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#2D0000', fill_color='#2D0000').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==6):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#1B0000', fill_color='#1B0000').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
    if(data['가격'].iloc[i]==0):
        folium.CircleMarker([map_alt[i],map_long[i]],radius=7, color='#FFFFFF', fill_color='#FFFFFF').add_child(folium.Popup(data['업소명'].iloc[i]+"\n"+string_price[i])).add_to(map_dong_price)
map_dong_price.save('map_all.html', encoding='utf-8') 


# 히트맵 출력
plt.subplot(2, 2, 1)
data_heatmap = data[["아메리카노", "근처 카페 수", "면적", "카페밀도", "인구밀도", "동 카페 수"]].copy()
plt.title('위도, 경도별 카페 분포 - 전체',fontsize=12)
sns.heatmap(data_heatmap.corr(), annot=True,cmap="YlGnBu",annot_kws={"size": 10})

plt.subplot(2, 2, 2)
data_heatmap1 = data_heatmap[(data["체인점"]==0)].copy()
plt.title('위도, 경도별 카페 분포 - 체인점 제외',fontsize=12)
sns.heatmap(data_heatmap1.corr(), annot=True,cmap="YlGnBu",annot_kws={"size": 10})

plt.subplot(2, 2, 3)
data_heatmap2 = data_heatmap[(data['아메리카노']!=0) ].copy()
plt.title('위도, 경도별 카페 분포 - 가격정보無 제외',fontsize=12)
sns.heatmap(data_heatmap2.corr(), annot=True,cmap="YlGnBu",annot_kws={"size": 10})

plt.subplot(2, 2, 4)
data_heatmap3 = data_heatmap1[(data['아메리카노']!=0) ].copy()
plt.title('위도, 경도별 카페 분포 - 체인점, 가격정보無 제외',fontsize=12)
sns.heatmap(data_heatmap3.corr(), annot=True,cmap="YlGnBu",annot_kws={"size": 10})
plt.show()

