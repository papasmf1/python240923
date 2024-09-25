#크롤링 선언 
from bs4 import BeautifulSoup

#html 파일 읽기
with open('Chap09_test.html', 'r', encoding='utf-8') as f:
    html = f.read()

#html 파싱
soup = BeautifulSoup(html, 'html.parser')

#cmd + /
# print(soup.prettify())

#문서에 있는 모든 <p> 태그 찾기
#print(soup.find_all('p'))

#첫번째 <p> 태그 찾기
#print(soup.find('p'))

#조건에 맞는 <p> 태그 찾기
#<p class="outer-text">필터링하기 
#print(soup.find_all('p', class_='outer-text'))
#최근에는 attrs속성 제공 
#print(soup.find_all('p', attrs={'class':'outer-text'}))

#<p>에서 id속성 검색
#print(soup.find_all('p', id='first'))

#찾은 결과를 루프돌리기
for p in soup.find_all('p'):
    #내부의 컨텐츠만 출력 
    title = p.text.strip()
    title = title.replace('\n', '')
    print(title)

    





