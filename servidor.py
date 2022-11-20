import socket

s = socket.socket()
s.bind(('127.0.0.1', 8000))
s.listen()
print('Inicializando servidor')

conn, address = s.accept()
print(address)

data = conn.recv(1024)
print('Recibir mensaje del cliente: {0}'.format(data.decode()))

conn.send('mensaje recibido'.encode())
conn.close()
s.close()
