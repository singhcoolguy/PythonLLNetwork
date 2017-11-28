#!/usr/bin/env python
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"""

def findIPv6RA(p):
	if p.haslayer(ICMPv6ND_RA):
		#print p.summary()
		#print p.display()
		print "RA with", p[ICMPv6NDOptPrefixInfo].prefix

sniff(prn = findIPv6RA)