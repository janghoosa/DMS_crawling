from flask import Flask
import urllib.request as req
import requests

app = Flask(__name__)
url_list : object = ''
temp = 0
ind = 0


@app.route('/')
def index():
    url = "127.0.0.1:5000/get"
    word = req.args.get('word')
    site = req.args.get('site')

    response = requests.get(url , params={
        'word' : word,
        'site' : site
    })

    url_list = response.content

    st = url_list.split('\n')
    urls : object = ''
    while st.count > ind:
        for i in range(10):
            urls = urls + st[ind] + '\n'
            ind = ind +1
        res = requests.get('127.0.0.1:5000/urls' , params = {
            'urls' : urls
        })





    return "success"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)