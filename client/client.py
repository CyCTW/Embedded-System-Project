import argparse
import socket
from module.GY801 import GY801
import time

parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('port')
args = parser.parse_args()

def main():
    try:
        sensor = GY801()
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((args.ip, int(args.port)))

        while True:
            aX, aaX, aaZ = sensor.getaX(), sensor.getaaX(), sensor.getaaZ()
            msg = b'No'
            if aaX < -100:
                msg = b'U'
            elif aaX > 40:
                msg = b'D'
            elif aaZ < -200:
                msg = b'L+S'
            elif aaZ > 200:
                msg = b'R+S'
            elif aX < -4:
                msg = b'L'
            elif aX > 4:
                msg = b'R'
            client.send(msg)
            data = client.recv(32)
            time.sleep(0.05)
                    
    except KeyboardInterrupt:
        print("Cleanup")


if __name__ == '__main__':
    main()
