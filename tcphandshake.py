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

send(i/t)