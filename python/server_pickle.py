import socket
import time
import pickle

HEADERSIZE=10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1236))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Conexion con {address} establecida exitosamente")

	msg = pickle.dumps("Bienvenido al server")
	msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg

	clientsocket.send(msg)

	while True:
		time.sleep(3)
		d = {1:"hi", 2: "there"}
		msg = pickle.dumps(d)
		msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8') + msg
		print(msg)
		clientsocket.send(msg)
		#clientsocket.close()