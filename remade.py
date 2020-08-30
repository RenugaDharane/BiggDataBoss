import requests
import bs4
import pandas as pd
result=requests.get("https://www.imdb.com/list/ls001896824/")
soup=bs4.BeautifulSoup(result.text,'lxml')
eng_mov=[]
tam_mov=[]
actor=[]
rating=[]
genre=[]
year=[]
emov=soup.select('.lister-item-header a')
for a in emov:
    eng_mov.append(a.text)
mgen=soup.select('.genre')
for b in mgen:
    genre.append(b.text)
genre[:]=[m.lstrip('\n') for m in genre]
genre=[m.rstrip('       ') for m in genre]
ac=soup.select('.list-description p')
b=[]

params = {
  "api_key": "tTUP2QTMLnM9",
  "format": "csv"
}
c = requests.get('https://www.parsehub.com/api/v2/projects/t3necMHtbcV7/last_ready_run/data', params=params)
b=c.text
d=b.split('\n')
d.pop(0)
d[:]= [title.lstrip('"') for title in d]
d[:]= [title.rstrip('"') for title in d]
for t in d:
    rating.append(float(t))
dr=[]
for c in ac:
    dr.append(c.text)
dr.pop(0)
r=[]
for b in dr:
    r.append(b.split('(')[0])
temp=r[98]
r[98]=temp[:19]
temp=r[96]
r[96]=temp[:16]
temp=r[95]
r[95]=temp[:6]
temp=r[94]
r[94]=temp[:10]
temp=r[93]
r[93]=temp[:5]
temp=r[92]
r[92]=temp[:9]
df = pd.DataFrame({'World_cinema':eng_mov,'Remade_tamil':r,'genre':genre,'rating':rating})
df.to_csv('remade.csv',index=False ,encoding='utf-8')