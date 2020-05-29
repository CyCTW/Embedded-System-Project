import socket
import argparse
import os
import threading
import time


def handle(client, addr):
	while True:
		try:
			text = client.recv(1024)

			# client input "quit"
			if text == 'quit\r\n' or not text:
				client.close()
			
			client.send(text)
			print(addr[0], addr[1], '>>', text)
		
		except Exception as e:
			print(e)
			print(addr[0], addr[1], '>>one client lose connection')
			break

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("HOST")
	parser.add_argument("PORT")
	args = parser.parse_args()

	host = args.HOST
	port = args.PORT
	
	s = socket.socket()


	s.bind( (host, int(port)) )
	s.listen(5)

	while True:
		client, addr = s.accept()
		print('Got connection from {}'.format(addr))
		
		# build thread to handle new client	
		threading._start_new_thread(handle, (client, addr) )

