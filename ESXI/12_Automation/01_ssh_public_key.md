# 자동화 
우리는 지금까지 서버를 주구장창 만들고, 보안정책만 만들기만 했다. 하지만 가장 중요한건 이런 수많은 서버들을 
통합적으로 보안점검을 하고 업데이트를 해야하는 시스템이 있어야 안정적이면서 효율적인 서버운영이 가능하다.  
이러한 솔루션을 가능하게 해주는 도구로 대표적으로 ansible이라는 도구가 있다.  
![google](./img/google.png)

## 잡소리
이러한 솔루션은 해커도 유용하게 사용하고있으며 이러한 기법을 활용한 대표적인 공격기법은 DDOS인데 하면은 범죄이니 절대로 하지말자.  
그리고 물론 chef나 superputty도 있으며 다양한 솔루션이 있는데 그중 가장 현대에 들어서 핫하며 최신 솔루션이 ansible이다.  
chef는 솔직히 안써봐서 뭐라 못하겠고 superputty는 소규모 서버를 대략 10개이하로 제어할떄 나름 괜찮지만 ansible처럼 통합적인 관리가 어렵다는 단점이 있다.  
salt는 최근에 써볼려고 했으나 하나하나 salt mini였나를 클라에 깔아야되서 아직 내 수준에선 ansible이 더 좋아보인다.

# ansible 설치

설치자체는 매우 간단하다

``` bash
sudo apt -y update &&\
apt -y install ansible
```

``` bash
vim /etc/ansible/hosts
```
> /etc/ansible/hosts

[webservers]  
10.10.1.2 ansible_user=server  
10.10.1.3 ansible_user=server  
10.10.1.4 ansible_user=server  

[ftp]
10.10.1.2 ansible_user=server

[db]
10.40.1.2 ansible_user=server

공개키 교환을 안하면은 에러가 뜰텐데 일단은 숫자가 적으니까  
각각 ssh로 접속하여 공개키 교환을 수동으로 하고 해주면된다.  

``` bash
ansible webservers -m ping -k
```

그리고 아래처럼 입력해주면은 기본세팅은 끝이다.

``` bash
ansible webservers -m "nslookup google.com" -k
```

# 비밀번호
상식적인 이야기지만 ssh는 공개키를 교환하면은 비밀번호를 입력하지않아도 ssh로 다른유저에게 접속이 가능하다.  
대표적 기능은 `ssh-copy-id` 기능을 이용한 공개키 교환이다.

이 공캐키를 배포하는 ansible-playgorund를 만들어보자

``` bash
ssh-keygen -t rsa 
```

``` yml
---
- name: Push SSH public key to client machines
  hosts: all
  tasks:
    - name: Add public key to authorized keys
      authorized_key:
        user: "{{ ansible_user }}"
        key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
```

위 ansible-playground를 실행할려면 아래와같이 사용해주자  
``` bash
ansible-playbook push-ssh-key.yml -k
```

이러면 모든 서버에 rsa로 암호화된 공개키를 /home/{{ ansible_user }}/.ssh/authorized_keys 로 전송이 된다.  