#!/usr/bin/env python
from scapy.all import *

"""Commands for SYN/ACK during Scapy:

Lengthen TCP Timeout to 10 mins:
	echo 10 > /proc/sys/net/ipv4/tcp_synack_retries

Block RST packets (Otherwise Kernel will consider scapy packets as unauthorized and prevent them from transmitting):
	iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP"""


e = Ether()
i = IP(dst = "10.0.2.15")
ic = ICMP()
p = e/i/ic
p.display()
srp1(p)

"""We can't change the dest MAC address as normal NICs (Network Interface Cards) verify the IP and Ether addresses against each other. 
However, Wireshark on the Win machine will lead to promiscuous mode, thus leading to accepting the packet."""

p[Ether].dst = WRONG_ADDR
srp1(p)