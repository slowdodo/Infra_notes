# ansible_console

ansible_console은 대충 명령어를 실시간으로 실행하게 해주는 도구다.  다양한 클라이언트들에게 간단한 작업들을 수행시킬떄 유용하다.  
이 기능을 바탕으로 간단하게 할수있는 보안점검을 할것이다.  

# 점검
가장 기본적인 점검인 passwd로 bash가 인가되지 않는 사용자에게 할당됐는지 점검하는것을 수행할것이다.

## /etc/passwd
``` bash
ansible all -m shell -a "cat /etc/passwd | grep bash " > passwd.txt.origin &&\
sed '/CHANGED/{x;p;x;}' passwd.txt.origin > passwd.txt &&\
rm -f  passwd.txt.origin
```

## /etc/shadow

``` bash
ansible all -m shell -a "cat /etc/shadow" -b -K > shadow.txt.origin &&\
sed '/CHANGED/{x;p;x;}' shadow.txt.origin > shadow.txt &&\
rm -f  shadow.txt.origin
```

## ufw status

``` bash
ansible all -m shell -a "ufw status" -b -K > ufw.txt &&\
sed '/CHANGED/{x;p;x;}' ufw.txt.origin > ufw.txt &&\
rm -f ufw.txt.origin
```

## group

``` bash
ansible all -m shell -a "cat /etc/group" -b -K > group.txt &&\
sed '/CHANGED/{x;p;x;}' group.txt.origin > group.txt &&\
rm -f group.txt.origin
```