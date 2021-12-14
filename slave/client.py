from kubernetes import client, config
from kubernetes.stream import stream

config = client.Configuration()

config.api_key['authorization'] = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
config.api_key_prefix['authorization'] = 'Bearer'
config.host = 'https://kubernetes.default'
config.ssl_ca_cert = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
config.verify_ssl = True

# api_client는 "2. 연결 정보 설정하기" 항목을 참고한다
api_client = client.CoreV1Api(client.ApiClient(config))

my_command = ['ls', '-l', '/tmp']

response = stream(api_client.connect_get_namespaced_pod_exec,
                  'pod name',
                  'namespace',
                  command=my_command,
                  stdin=False,
                  stderr=True,
                  stdout=True,
                  tty=False)

print(response)
