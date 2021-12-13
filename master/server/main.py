from kubernetes import client, config
from kubernetes.stream import stream

# create an instance of the API class

config.load_kube_config()
api_client = client.CoreV1Api()