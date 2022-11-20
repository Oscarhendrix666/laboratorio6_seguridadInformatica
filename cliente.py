import socket

s = socket.socket(('127.0.0.1', 8000))
s.connect(('127.0.0.1', 8000))

s.send(b'Saluda cliente')
data = s.recv(1024)
print('Recive mensaje desde el servidor: {0}'.format(data.decode()))

s.close()
