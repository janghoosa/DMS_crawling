from flask import Flask
import urllib.request as req
import requests

# app = Flask(__name__)
url_list : object = ''
temp = 0
ind = 0
suc = 0
fail = 0
total = 0


def index():
    url = "127.0.0.1:5000/get"

    word = input('검색어 : ')
    site = input('검색할 사이트( 네이버, bing 중 하나 ) : ')

    # word = req.args.get('word')
    # site = req.args.get('site')

    response = requests.get(url , params={
        'word' : word,
        'site' : site
    })

    url_list = response.content

    st = url_list.split('\n')

    total = st.count
    suc = 0
    fail = 0
    print("total : "+total+" images , success download : " + suc +" , failed download : "+fail)

    urls : object = ''
    while st.count > ind:
        for i in range(10):
            urls = urls + st[ind] + '\n'
            ind = ind +1
        res = requests.get('127.0.0.1:5000/urls' , params = {
            'urls' : urls
        })
        if ( res == 'success'):
            suc = suc + 10
            print("total : "+total+" images , success download : "+suc +" , failed download : "+fail)
        else:
            fail = fail + 10
            print("total : "+total+" images , success download : "+suc +" , failed download : "+fail)
    
    print("total : "+total+" images , success download : "+suc +" , failed download : "+fail)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    while( True ) :
        index()

        word = input('종료하시겠습니까?(y/n) : ')
        if word =='y':
            break