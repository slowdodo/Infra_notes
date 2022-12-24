# ansible_console

ansible_console은 대충 명령어를 실시간으로 실행하게 해주는 도구다.  다양한 클라이언트들에게 간단한 작업들을 수행시킬떄 유용하다.  
이 기능을 바탕으로 간단하게 할수있는 보안점검을 할것이다.  

# 점검
가장 기본적인 점검인 passwd로 bash가 인가되지 않는 사용자에게 할당됐는지 점검하는것을 수행할것이다.  
보통 저런 기본적인건 수동으로 점검하진 않고 자동화 시키지만 배쉬 명령어들을 한번 본다는 관점에서 적어봤다.  

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

# lynsis

기본적인 보안 결함들을 빠르게 찾아주는 도구로 주정통, 국정원 메뉴얼처럼 타이트하지는 않지만  
오픈소스이며 표준 패키지에 항상 포함되있는 등 다양한 장점으로 여러가지로 사용되는 도구이다.  
우리는 이 도구를 사용할것이다.  

``` bash
ansible all -m shell -a "lynis audit system --warnings-only" -b -K > WARNING.txt
```

> WARNING.txt

``` bash
10.10.1.4 | CHANGED | rc=0 >>
    - Permissions for directory: /etc/sudoers.d               [ WARNING ]
    - Minimal of 2 responsive nameservers                     [ WARNING ]
  - Permissions of home directories                           [ WARNING ]
10.10.1.2 | CHANGED | rc=0 >>
    - Permissions for directory: /etc/sudoers.d               [ WARNING ]
  - Checking vulnerable packages                              [ WARNING ]
    - Minimal of 2 responsive nameservers                     [ WARNING ]
  - Permissions of home directories                           [ WARNING ]
10.40.1.2 | CHANGED | rc=0 >>
    - Permissions for directory: /etc/sudoers.d               [ WARNING ]
  - Checking vulnerable packages                              [ WARNING ]
    - Minimal of 2 responsive nameservers                     [ WARNING ]
  - Permissions of home directories                           [ WARNING ]
10.11.1.2 | CHANGED | rc=0 >>
    - Permissions for directory: /etc/sudoers.d               [ WARNING ]
    - Minimal of 2 responsive nameservers                     [ WARNING ]
  - Permissions of home directories                           [ WARNING ]
  - Ownership of home directories                             [ WARNING ]
10.10.1.3 | CHANGED | rc=0 >>
    - Permissions for directory: /etc/sudoers.d               [ WARNING ]
    - Minimal of 2 responsive nameservers                     [ WARNING ]
  - Permissions of home directories                           [ WARNING ]
```