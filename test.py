import os

stream = os.popen('kubectl get pods -o yaml | grep podIP')
output = stream.read()
ip = output.split(':')[1].replace(' ','').split('\n')[0]
print(ip)