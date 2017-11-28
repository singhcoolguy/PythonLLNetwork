#!/usr/bin/env python
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"""


def findSYN(p):
	flags = p.sprintf("%TCP.flags%")
	if flags == "S":
		ip = p[IP]
		tcp = p[TCP]
		i = IP(dst = ip.src, src = ip.dst)
		t = TCP(sport = tcp.dport, dport = tcp.sport, seq = tcp.ack,ack = tcp.seq + 1) #new_ack
		print "SYN/ACK sent to" + i.dst + ':' + t.dport
		send(i/t)

sniff(prn = findSYN)