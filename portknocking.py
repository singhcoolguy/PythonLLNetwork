import socket

s = socket.socket()
s.settimeout(3)

p = input("Port Number: ")
try:
	s.connect(("packtpub.samsclass.info", int(p)))
	st = s.recv(1024).decode("utf-8")
	s.close()
	s = socket.socket()
	s.settimeout(3)
	s.connect(("packtpub.samsclass.info", int(st.split()[5][:-1])))
	print(s.recv(1024))
	s.close()
except Exception as e:
	print(e)
