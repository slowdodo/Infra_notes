---
layout: post
title:  "ESXI 인프라 구축방법-2 vSphere설치 "
---

# 준비사항
1. Window10 이상 
2. VMware 15 이상 버전
3. 하드 용량 200GB 이상
4. 메모리 16기가 이상
5. vShpere 8.0

# 목록
- [준비사항](#준비사항)
- [목록](#목록)
- [vSphere 운영체제 설치방법 1 - 운영체제 다운로드](#vsphere-운영체제-설치방법-1---운영체제-다운로드)
- [vSphere 운영체제 설치방법 2 - VMware에 설치 세팅](#vsphere-운영체제-설치방법-2---vmware에-설치-세팅)
- [vSphere 운영체제 설치방법 3 - 네트워크 설정](#vsphere-운영체제-설치방법-3---네트워크-설정)
- [vSphere 운영체제 설치방법 4 - vSphere 실제 설치](#vsphere-운영체제-설치방법-4---vsphere-실제-설치)


VMware 설치는 너무 많으니 생략하고 vSphere 설치부터 진행하겠다.
간단한 인프라 구축을 할것이기 떄문에 더 자세한 내용은
[VMware 6.5 document](https://docs.vmware.com/kr/VMware-vSphere/6.5/vsphere-esxi-vcenter-server-651-installation-setup-guide.pdf) 이것을 참고하는것을 추천한다.

-------------

# vSphere 운영체제 설치방법 1 - 운영체제 다운로드
[Download vSphere link](https://customerconnect.vmware.com/downloads/info/slug/datacenter_cloud_infrastructure/vmware_vsphere/8_0)
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcccJtg%2FbtrO5s7uXuC%2FeZMFacW7zqIiPj64BDaUbK%2Fimg.png" >

아래로 들어가면은 로그인 화면이 나오는데 로그인 하고 다운로드 하면은 된다.
유로 서비스 이기에 trial 30일 이용을 선택하면은 OS의 `.iso`이 나오는데 그걸로 설치하는거다.

------
# vSphere 운영체제 설치방법 2 - VMware에 설치 세팅

vmware net Virtual Macine 누르기
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fedplh7%2FbtrOQrBxKSj%2FYR5PcEQGKCIYgSFtuEtqh1%2Fimg.png" width=300><br>
<br>

recoomanded 들어가기
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbDBrQA%2FbtrOD4tTyJn%2FSiVVPTIzF9KBYPanOvskO1%2Fimg.png">
<br>
다운받은 운영체제 넣기
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FlIAcu%2FbtrOQEAR893%2Fn80mv6mx0s3HoCEPc1pmgk%2Fimg.png" width=800>
<br>

VMware ESX 클릭후 Version을 아래와같이 설정
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbx2v9O%2FbtrOQudWQcD%2F78AFrF7Vpw3i1kfuaBJqJ1%2Fimg.png">
<br>

그 후로 설정은 사양따라 적당히 타협하며 진행하면 된다
<br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fy7Bve%2FbtrO6gyOkcD%2FxD3m9kG6s9IWHkVR2oAD71%2Fimg.png">
<br>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb6mw3A%2FbtrO44MzWVA%2F1PrfVwphJfBkxlKsjBgJp1%2Fimg.png">

-----

# vSphere 운영체제 설치방법 3 - 네트워크 설정 

여기서부터는 네트워크 설정이다. 
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fm5fGK%2FbtrO5ssV6px%2F4aj1IyCAZQO7XDkeKfKUD1%2Fimg.png">

<br>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCFbtH%2FbtrO5r1OIdj%2FGmwyalwKVC2jYWquXHkThK%2Fimg.png">

<br>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fln8rT%2FbtrO5s7vqL3%2FyPk82QwnKv5GzkUtTFP0K1%2Fimg.png">
<br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fdw5ulJ%2FbtrO44TjLHt%2FCYTan7HZpvFwqJQ583VkeK%2Fimg.png">

일단 따라하자, 위와같이 Briged Automatic으로 2개
Host Only로 1개로 총 3개의 가상 NIC을 만들어준다.

아래와 같은 네트워크 구조를 만들기 위해서 위와같이 3개의 가상의 NIC을 만들어주는것이다.
<br>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbPzGlA%2FbtrOQDWjkJW%2FKUXV8O8wVQv0C6Blgk3Xwk%2Fimg.png">

그러면 우리가 만든 3개의 NIC은 무슨 역할을 할까? 아래와 같은 역할을 한다.

1. Bridge Mode로 설정(WAN2 역할, vSphere 접속용)
2. Bridge Mode로 설정(WAN1 역할)
2. Host Only로 설정(LAN 역할)

어디서 많이 본거같은데 실제 인프라를 가상으로 구축해보는것이다. 

참고로 Host Only mode의 구성은 아래와 같다.
<br>
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcYh2a1%2FbtrOQGleqYz%2F8QGvQdM02nZMbW6GrQX2A0%2Fimg.png">

---------
# vSphere 운영체제 설치방법 4 - vSphere 실제 설치

설치 자체는 쉽다. 그냥 가만히 있으면 설치된다.
<br>
![설치](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbRFygD%2FbtrO5r8EjkH%2FY175NBCjVefi61pGXKNGbK%2Fimg.png)

설치가 다 되면은 아래와 같이 나올것이다.
<br>
![vSpher 설치](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Frubpx%2FbtrOQDWh1Tn%2FNSs1gTTpAPdCiG5JePOTj0%2Fimg.png)

저기 나오는 IPv4 주소로 접속해주면은 기본적인 세팅 자체는 끝이다.
