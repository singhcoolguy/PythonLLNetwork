#!/usr/bin/env python
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"""

ipaddr = []
macaddr = []

def findARP(p):
	if p.haslayer(ARP):
		#print p.summary()
		#print p.display()
		n = len(ipaddr)
		old = 0

		for i in range(n):
			if ipaddr[i] == p.psrc:
				old = 1
				if p.hwsrc != macaddr[i]:
					print "ARP Poisoned"
					print ipaddr[i], "moved from ", macaddr[i], "to", p.hwsrc
		if old == 0:
			ipaddr.append(p.psrc)
			macaddr.append(p.hwsrc)
			print "New Host: ", p.psrc, p.hwsrc

sniff(prn = findARP)