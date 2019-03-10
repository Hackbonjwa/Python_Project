import requests
from bs4 import BeautifulSoup

url = 'https://naver.com'
html = requests.get(url)

bs_obj = BeautifulSoup(html.content, 'html.parser')

ul_class = bs_obj.find('ul',{'class':'ah_l'})
span_class = ul_class.findAll('span',{'class':'ah_k'})
for n,i in enumerate(span_class):
    print(n,'위 : ',i.text)