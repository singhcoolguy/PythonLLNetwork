#!/usr/bin/env python3
from scapy.all import *

conf.L3socket
conf.L3socket = L3RawSocket

i = IP(dst = "packtpub.samsclass.info")
t = TCP(dport = 80)

r = sr1(i/t)

t.flags = 'A'
t.ack = r.seq + 1
t.seq = r.ack

req = "GET / HTTP/1.1\r\n" + \
"HOST: packtpub.samsclass.info\r\n\r\n"
send(i/t/req)

reply = sniff(4)
wireshark(reply)