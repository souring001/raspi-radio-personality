import socket

ip = '192.168.170.58'
port = 51451

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((ip, port))
	s.listen(1)
	

	conn, addr =s.accept()
	with conn:
		while True:
			data = conn.recv(1024)
			if not data:
				continue
			print('data : {}, addr: {}'.format(data,addr))
			conn.sendall(b'milk boy')
