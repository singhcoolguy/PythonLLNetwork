import socket


#p = input("Port Number: ")
for p in range(3000,4001):
	try:
		s = socket.socket()
		s.settimeout(3)
		print(p)
		s.connect(("packtpub.samsclass.info", p))
		print(s.recv(1024))
		s.close()
	except Exception as e:
		pass
