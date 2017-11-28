#!/usr/bin/env python
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"""

def findDNS(p):
	if p.haslayer(DNS):
		#print p.summary()
		#print p.display()
		print p[IP].src, p[DNS].summary()

sniff(prn = findDNS)