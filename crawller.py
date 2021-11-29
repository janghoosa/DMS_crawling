from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' # 네이버 검색url
plusUrl = input('검색어를 입력하세요 : ') # 검색어 질문
url = baseUrl + quote_plus(plusUrl) # url로 이동하기위한 쿼리문자열 만들기

print(url)
html  = urlopen(url) # url 열기
bsObject = BeautifulSoup(html, 'html.parser')

# for img in bsObject.find_all(name="img",limit=10):
#     print(img['src'])

n = 1
for img in bsObject.find_all(name="img",limit=10): # 이미지를 50개 저장하기 위한 반복문
    imgUrl = img['src']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n)+'.jpg','wb') as h: # 이미지 + 사진번호 + 확장자는 jpg
            img = f.read() #이미지 읽기
            h.write(img) # 이미지 저장
    n += 1
print('다운로드 완료')