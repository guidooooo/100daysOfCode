import socket
import time

HEADERSIZE=10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1233))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexion con {address} establecida exitosamente")

	msg = "Bienvenido al server"
	msg = f"{len(msg):<{HEADERSIZE}}" + msg

	clientsocket.send(bytes(msg, 'utf-8'))

	while True:
		time.sleep(3)
		msg = f"Seguimos conectados, son las {time.time()}"
		msg = f"{len(msg):<{HEADERSIZE}}" + msg
		clientsocket.send(bytes(msg, 'utf-8'))
		#clientsocket.close()