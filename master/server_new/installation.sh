#쿠버네티스 runtime(docker) 설치
#패키지 관리 도구 업데이트
sudo apt update
sudo apt-get update
# 기존에 설치된 docker 삭제 후 재설치
sudo apt-geet remove docker docker-engine docker.io
# docker에 필요한 라이브러리 설치
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
# docker 설치 18.06 설치
sudo apt-get intall docker-ce=18.06.2~ce~3~0~ubuntu -y

# 쿠버네티스 설치
# APT 추가
sudo apt install apt-transport-https
# curl 명령어로 gps key 내려받기
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
# 키 확인
sudo apt-key fingerprint 0EBFCD88
# 패키지 관리 도구에 repository 추가
sudo add-apt-repository "deb https://apt.kubernetes.io/ kubernetes-$(lsb_release -cs) main"
# 패키지 관리도구 업데이트
sudo apt-get update
# 패키지 설치
sudo apt install kubelet kubeadm kubectl
# 패키지 환경설정 고정
sudo apt-mark hold kubelet kubeadm kubectl

# kubelet 버전 확인
kubelet --version
# kubeadm 버전 확인
kubeadm version
# kubectl 버전 확인
kubectl version