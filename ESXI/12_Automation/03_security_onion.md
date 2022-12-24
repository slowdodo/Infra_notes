# security onion
ftp 서버에 filebeat, metricbeat, auditbeat이 올려졌고 모두 다운로드가 가능하다는 가정하에 진행할것이다.  

# deb 패키지 배포및 설치

[ftp_file](./rule/ftp_file.yml)  
``` bash
ansible-playground ftp_file.yml -b -K
```

# 확인
``` bash
ansible-console -b -K
```
``` bash
ls| grep '\.deb' | cut -d "-" -f1
```
``` bash
dpkg --list | grep beat | awk '{print $2}'
```

# 