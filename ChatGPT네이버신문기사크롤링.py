import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 크롤링할 URL 설정
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

# 페이지 요청
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # 신문 기사 제목을 추출하는 CSS 선택자 지정
    titles = soup.select('.news_tit')

    # 엑셀 파일 생성
    wb = Workbook()
    ws = wb.active
    ws.title = "뉴스 크롤링"

    # 엑셀 파일에 헤더(열 제목) 추가
    ws.append(['Title', 'URL'])

    # 추출한 기사 제목과 URL을 엑셀 파일에 추가
    for title in titles:
        ws.append([title.get_text(), title['href']])

    # 엑셀 파일 저장
    wb.save("results.xlsx")

    print("크롤링한 결과가 results.xlsx 파일로 저장되었습니다.")
else:
    print("페이지를 불러오는 데 실패했습니다.")
