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

# yml파일 사용하여 beats으로 log를 SO에 배포
사실 여기서부턴 완전 자동화보단 반자동화에 가까운 작업이다.  
로그를 싹다 통합적으로 묶어서 siem에 전달하면은 상당히 비효율적이고 피곤한 시스템이 되어버리기 떄문이다.  
각각 호스트별로 정해놓은 목적과 수집할 로그를 정확하게 나눠서 효과적인 playground를 작성해야 효과적인 자동화 배포가 될수있는데 이것까지하기엔 내 수준이 그리 높지가 않다.  
그렇기에 어떻게 beats를 작성하여 한곳에서 여러곳으로 배포하는지를 보여주기만 할것이다.  
각자의 수준에 맞게 이러한 예제를 보고 ansible이 뭐하는건지를 파악하고 커스텀하여 스킬을 업그레이드하길 바란다.  

# filebeat
[filebeat](./beat/filebeat.yml)  

``` bash
#output.logstash:
  # The Logstash hosts
  #hosts: ["localhost:5044"]

  # Optional SSL. By default is off.
  # List of root certificates for HTTPS server verifications
  #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

  # Certificate for SSL client authentication
  #ssl.certificate: "/etc/pki/client/cert.pem"

  # Client Certificate Key
  #ssl.key: "/etc/pki/client/cert.key"
```

``` bash
output.logstash:
  # The Logstash hosts
  hosts: ["192.168.2.10:5044"]

  # Optional SSL. By default is off.
  # List of root certificates for HTTPS server verifications
  #ssl.certificate_authorities: ["/etc/pki/root/ca.pem"]

  # Certificate for SSL client authentication
  #ssl.certificate: "/etc/pki/client/cert.pem"

  # Client Certificate Key
  #ssl.key: "/etc/pki/client/cert.key"
```