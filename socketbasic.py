import socket

s = socket.socket()
s.settimeout(3)

p = input("Port Number: ")
try:
	s.connect(("packtpub.samsclass.info", int(p)))
	print(s.recv(1024))
	s.close() 
except Exception as e:
	print(e)
