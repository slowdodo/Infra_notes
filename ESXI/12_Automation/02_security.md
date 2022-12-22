# 방화벽 설치
기본적으로 리눅스에는 iptables 라는 커널에 탑재된 netfilters라는 기능을 서포트 해주는 툴이 설치되어있다.  
하지만 우리는 ufw라는 데비안 계열에서 만든 iptables를 좀더 쉽게 다룰수있게 만든 기능을 사용할것이다.  
기본적으로 ufw는 all deny정책을 수행하기에 잘못 포트를 닫는순간 대참사가 발생하니 주의해서 rule을 작성하고 관리해야한다.

# 시작

루트로 로그인하고 apt이란 모듈을 이용하여 ufw를 설치하라는 간단한 ansible 스크립트이다.  

``` bash
ansible all -m apt -a "name=ufw state=present" -b -K
```

[ufw_basic](./rule/ufw_rule.yml)  

위 소스코드를 만들어서 아래와같이 실행하면 위 룰처럼 실행될것이다.

``` bash
ansible-playground ufw_rule.yml
```
