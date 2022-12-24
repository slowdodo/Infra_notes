1. /etc/ansible/hosts의 ansible_user이름이 올바른가?
2. /etc/ansible/hosts의 패스워드를 암호화한 상태로 입력했는가?(암호화 하지않는 상태면은 default를 복호화 해서 전송해서 암호가 이상해지기도 함)
3. root가 필요한 옵션인데 -b라는 옵션을 주지않았는가?
4. -b 다음에 -K 대신에 -k를 입력하였는가?
5. 접속한 user가 sudo 권한을 가지지 못했는가?