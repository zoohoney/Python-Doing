import pandas as pd
#df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
#print(df)
#df[1]
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',header=0,index_col=0)
df[1]
summer = df[1].iloc[:,:5]
summer.columns = ['경기수','금','은','동','계']
summer
print(summer.sort_values('금',ascending=False))
summer.to_excel('하계올림픽메달.xlsx') #엑셀 파일로 저장
index = pd.date_range('1.1.2000',periods=8) # 8개 인덱스 만듬
print(index)
import numpy as np 
df = pd.DataFrame(np.random.rand(8,3), index = index, columns=list('ABC'))
df
print(df['B']) # 보고싶은 열 검색 
print(df['B'] > 0.4) #마스크 기능 조건 걸기 
df2 = df[df['B'] > 0.4]
df2
df2.T #T 는 행과 열을 바꿔줌 
index = pd.date_range('1.1.2021',periods=8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns=list('ABC'))
df['D'] = df['A'] / df['B']
df