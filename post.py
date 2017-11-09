import socket

s = socket.socket()
s.settimeout(2)

target = 'packtpub.samsclass.info'
s.connect((target, 80))
un = 'root'
pw = 'password'
length = len(un) + len(pw) + 5

req = """POST /http/login1.php HTTP/1.1
Host: packtpub.samsclass.info
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Referer: http://packtpub.samsclass.info/http/login1.htm
Content-Type: application/x-www-form-urlencoded
Content-Length: {length}
Connection: keep-alive
Upgrade-Insecure-Requests: 1

u={un}&p={pw}"""
req = req.format(length = length, un = un, pw = pw)
print('Request:\n', req)

s.send(req.encode('utf-8'))
print('Response:\n')
print(s.recv(1024).decode('utf-8'))

s.close()