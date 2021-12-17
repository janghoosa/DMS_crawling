from flask import Flask
import urllib.request as req
import requests
import asyncio

# app = Flask(__name__)
url_list : object = ''
temp = 0
ind = 0
suc = 0
fail = 0
total = 0

# from kubernetes import client, config, watch

# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()

# v1 = client.CoreV1Api()
# count = 10
# w = watch.Watch()
# for event in w.stream(v1.list_namespace, _request_timeout=60):
#     event['object'].
#     print("Event: %s %s" % (event['type'], event['object'].metadata.name))
#     count -= 1
#     if not count:
#         w.stop()

# print("Ended.")


# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()

# v1 = client.CoreV1Api()
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def index():
    # config.load_kube_config()

    # v1 = client.CoreV1Api()
    # print("Listing pods with their IPs:")
    # ret = v1.list_pod_for_all_namespaces(watch=False)
    # for i in ret.items:
    #     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    url = "127.0.0.1:5000/"

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
    print("[START] total : "+total+" images , success download : "+suc)

    urls : object = ''
    while st.count > ind:
        for i in range(10):
            urls = urls + st[ind] + '\n'
            ind = ind +1

        loop = asyncio.get_event_loop()
        loop.run_until_complete( res =  getImage(urls))
        loop.close()

        suc = suc + 10
        print("[CONTINUE] total : "+total+" images , success download : "+suc)
    
    print("[FIN] total : "+total+" images , success download : "+suc)

async def getImage(urls):
    res = requests.post('127.0.0.1:5000/urls' , params = {
            'urls' : urls
        })

    return res

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    while( True ) :
        index()

        word = input('종료하시겠습니까?(y/n) : ')
        if word =='y':
            break