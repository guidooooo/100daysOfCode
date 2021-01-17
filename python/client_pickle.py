import socket
import pickle

HEADERSIZE=10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1236))

while True:
	full_msg = b''
	new_msg = True

	while True:
		msg = s.recv(16)
		if new_msg:
			print(f"Nuevo mensaje recibido, su largo es {msg[:HEADERSIZE]}")
			msglen = int(msg[:HEADERSIZE])
			new_msg = False

		print(f"full message length: {msglen}")	
		full_msg += msg

		if len(full_msg) - HEADERSIZE == msglen:
			print("mensaje recibido complemente")
			d = pickle.loads(full_msg[HEADERSIZE:])
			print(d)
			new_msg = True
			full_msg = b''