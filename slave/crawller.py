from urllib.request import urlopen
from urllib.parse import quote_plus
from flask import Flask
from bs4 import BeautifulSoup
import os

LIMIT = 50

app = Flask(__name__)

def createFolder(directory):  # 이미지 저장할 폴더를 생성하는 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error:Creating directory. ' + directory)


def downloadPic():  # 이미지를 다운받는 함수
    n = 1
    for img in bsObject.find_all(name="img", limit=LIMIT):  # 이미지를 50개 저장하기 위한 반복문
        imgUrl = parseImgUrl(img)
        if "http" in imgUrl:
            with urlopen(imgUrl) as f:
                with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                    img = f.read()  # 이미지 읽기
                    h.write(img)  # 이미지 저장
                    if (n % 10 == 0):
                        print('%i Done' % n)
        n += 1
    print('Download Complete')


def showListImageSrc():
    for img in bsObject.find_all(name="img", limit=LIMIT):
        imgUrl = parseImgUrl(img)
        if "http" in imgUrl:
            print(imgUrl)  # 이미지의 src를 출력하는 부분


def saveURLtoFile():
    n = 1
    with open('./' + 'urlList' + '.txt', 'w') as f:
        for img in bsObject.find_all(name="img", limit=LIMIT):  # 이미지를 50개 저장하기 위한 반복문
            imgUrl = parseImgUrl(img)
            if "http" in imgUrl:
                print(imgUrl)
                f.write(imgUrl + "\n")
            if (n % 10 == 0):
                print('%i Done' % n)
            n += 1


def loadDataFromFile():
    with open('/resUrlList.txt', 'r') as f:
        imgUrl = f.readlines()
        print(imgUrl)

def parseImgUrl(img):
    imgUrl = img['src']
    imgUrl = imgUrl.split('?w=')[0]
    imgUrl = imgUrl.split('&type')[0]
    return imgUrl

baseUrl1 = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='  # 네이버 검색url
baseUrl2 = 'https://www.bing.com/images/search?q=' # bing 검색

def select():
    while (1):
        try:
            url = loadDataFromFile()
        except :
            print("no file")
            plusUrl = input('Input searchword : ')  # 검색어 질문
            selectUrl = input('Input url: 1 or 2')
            if selectUrl == '1':
                baseUrl = baseUrl1
            elif selectUrl == '2':
                baseUrl = baseUrl2
            else:
                baseUrl = baseUrl1
            url = baseUrl + quote_plus(plusUrl)  # url로 이동하기위한 쿼리문자열 만들기

            print(url)
            html = urlopen(url)  # url 열기
            bsObject = BeautifulSoup(html, 'html.parser')

        # print(os.getcwd()) # os에서 현재 주소를 가져옴

        ifDownload = input('Do you want to download it? y or n')
        if ifDownload == 'y':
            createFolder('img')
            downloadPic()

        ifShowList = input('Do you want to see URL? y or n')
        if ifShowList == 'y':
            showListImageSrc()

        ifSaveList = input('Do you want to save URL? y or n')
        if ifSaveList == 'y':
            saveURLtoFile()

        ifExit = input('Are you exit? y or n')
        if ifExit == 'y':
            break

@app.route('/')
def index():
    return "Hello!!"

@app.route('/get')
def get():
    print("get")
    word = request.args.get('word')
    site = request.args.get('site')
    if site == 'naver':
        baseUrl = baseUrl1
    elif site == 'bing':
        baseUrl = baseUrl2
    else:
        baseUrl = baseUrl1
    url = baseUrl + quote_plus(word)
    html = urlopen(url)  # url 열기
    bsObject = BeautifulSoup(html, 'html.parser')
    res : object = ''
    for img in bsObject.find_all(name="img", limit=LIMIT):
        imgUrl = parseImgUrl(img)
        if "http" in imgUrl:
            res = res + imgUrl + "\n"
    return res

@app.route('/get/url')
def download():
    print("/get/url/")
    UrlListGet = request.args.get('url')
    n = 0
    for url in UrlListGet:
        if "http" in url:
            with urlopen(url) as f:
                with open('./img/' + plusUrl + str(n) + '.jpg', 'wb') as h:  # 이미지 + 사진번호 + 확장자는 jpg
                    img = f.read()  # 이미지 읽기
                    h.write(img)  # 이미지 저장
                    if (n % 10 == 0):
                        print('%i Done' % n)
        n += 1
    print('Download Complete')
    return "Download Complete"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
