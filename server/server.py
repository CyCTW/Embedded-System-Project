import socket
import argparse
import os
import threading
import time
import keyboard
import pyautogui as ptg

parser = argparse.ArgumentParser()
parser.add_argument("HOST")
parser.add_argument("PORT")
parser.add_argument("Game")

args = parser.parse_args()

keymap1 = {'L': 'left', 'U': 'up', 'D': 'enter', 'R': 'right', 'L+S': 'left+enter', 'R+S': 'right+enter'}
keymap2 = {'L' : 'd', 'U' : 'r', 'D' : 'z', 'R' : 'g', 'L+S': 'd+z', 'R+S': 'g+z'}

keymap3 = {'L': 'left', 'R': 'right'}
keymap4 = {'L' : 'z', 'R': 'x'}

prev_cmd1 = "l"
prev_cmd2 = "l"


def keypress(cmd, numb):
	global prev_cmd1
	global prev_cmd2


	#cmd = cmd.replace(" ", "+")
	
	#time.sleep(0.03)

	if numb == 1:
		'''
		if cmd == "enter":
			keyboard.release(cmd)
			keyboard.press(cmd)			
			time.sleep(0.03)
			keyboard.release(cmd)
			
			keyboard.press(cmd)
			time.sleep(0.03)
			keyboard.release(cmd)

			keyboard.press(cmd)
			time.sleep(0.03)
			keyboard.release(cmd)
			keyboard.press
		'''
		if cmd != prev_cmd1:
			keyboard.release(prev_cmd1)
				
			keyboard.press(cmd)
		prev_cmd1 = cmd

	elif numb == 2:
		if cmd != prev_cmd2:
			keyboard.release(prev_cmd2)
			keyboard.press(cmd)
		prev_cmd2 = cmd


# transform command to keyboard signal
def Pika_act(cmd, numb):
	global prev_cmd1
	global prev_cmd2

	ply_cmd = ""
	if numb == 1:
		if cmd not in keymap1.keys():
			if prev_cmd1 != "l":
				keyboard.release(prev_cmd1)

			prev_cmd1 = "l"
			return "key error"
		else:
			
			keypress(keymap1[cmd], 1)
			ply_cmd = keymap1[cmd]

	elif numb == 2:
		if cmd not in keymap2.keys():
			if prev_cmd2 != "l":
				keyboard.release(prev_cmd2)

			prev_cmd2 = "l"
			return "key error"
		else:
			keypress(keymap2[cmd], 2)
			ply_cmd = keymap2[cmd]
	
	print( "{} command send: {}".format("player" + str(numb), ply_cmd) )
	return "{} command send: {}".format("player" + str(numb), ply_cmd)


def Down_act(cmd, numb):
	global prev_cmd1
	global prev_cmd2

	ply_cmd = ""
	if numb == 1:
		if cmd not in keymap3.keys():
			if prev_cmd1 != "l":
				keyboard.release(prev_cmd1)

			prev_cmd1 = "l"
			return "key error"
		else:
			
			keypress(keymap3[cmd], 1)
			ply_cmd = keymap1[cmd]

	elif numb == 2:
		if cmd not in keymap4.keys():
			if prev_cmd2 != "l":
				keyboard.release(prev_cmd2)

			prev_cmd2 = "l"
			return "key error"
		else:
			keypress(keymap4[cmd], 2)
			ply_cmd = keymap2[cmd]
	
	print( "{} command send: {}".format("player" + str(numb), ply_cmd) )
	return "{} command send: {}".format("player" + str(numb), ply_cmd)

def Mouse_act(cmd):
	if cmd == "L":
		ptg.move(-30, 0)	
	elif cmd == "R":
		ptg.move(30, 0)
	elif cmd == "u":
		ptg.move(0, 30)
	elif cmd == "d":
		ptg.move(0, -30)
	elif cmd == "U":
		ptg.click()
	
	return "command send: {}".format(cmd)

def handle(client, addr, numb):
	st = "You are player" + str(numb)
	st = st.encode()
	client.send(st)
	while True:
		try:
			
			text = client.recv(1024).decode()
			
			game = args.Game
		
			if game == "Pika":
				res = Pika_act(text, numb)
			elif game == "Down":
				res = Down_act(text, numb)
			elif game == "Mouse":
				res = Mouse_act(text)
			else:
				pass
			client.send(res.encode())

			# client input "quit"
			if text == 'quit\r\n' or not text:
				client.close()

			
# print(addr[0], addr[1], '>>', text)
		
		except Exception as e:
			print(e)
			print(addr[0], addr[1], '>>one client lose connection')
			break

if __name__ == "__main__":

	host = args.HOST
	port = args.PORT
	
	s = socket.socket()


	s.bind( (host, int(port)) )
	s.listen(5)
	numb = 1

	while True:
		client, addr = s.accept()
		# addr[0]: ip address, addr[1]:port number
		print(client)
		print('Got connection from {}'.format(addr))
		
		# build thread to handle new client	
		threading._start_new_thread(handle, (client, addr, numb) )
		numb += 1

