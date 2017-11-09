import socket

s = socket.socket()
s.settimeout(2)

target = 'packtpub.samsclass.info'
s.connect((target, 80))

req = 'GET / HTTP/1.1\nHost: ' + target + '\n\n'
print('Request:\n', req)

s.send(req.encode('utf-8'))
print('Response:\n', s.recv(1024).decode('utf-8'))

s.close()