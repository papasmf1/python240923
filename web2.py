# web2.py 
#웹서버에 페이지 실행 요청
import requests
#크롤링 라이브러리 
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

#검색이 용이한 스프객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

#상단의 <div>태그 검색 
#파일로 저장 
f = open("daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all('div', attrs={'class':'card-desc'})    
for post in posts:
    titleElem = post.find('h2', attrs={'class':'card-title'})
    priceElem = post.find('div', attrs={'class':'card-price'})
    regionElem = post.find('div', attrs={'class':'card-region-name'})
    title = titleElem.text.strip()
    price = priceElem.text.strip()
    region = regionElem.text.strip()
    #f-string 포맷팅(포맷스트링)
    print(f"{title}, {price}, {region}")
    f.write(f"{title}, {price}, {region}\n")

f.close()

#  <div class="card-desc">
#       <h2 class="card-title">아이폰 14 128GB</h2>
#       <div class="card-price ">
#         600,000원
#       </div>
#       <div class="card-region-name">
#         전남 순천시 용당동
#       </div>