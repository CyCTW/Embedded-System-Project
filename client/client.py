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

        delay = 0.02
        while True:
            aX, aY, aaZ = sensor.getaX(), sensor.getaY(), sensor.getaaZ()
            if aY > 4:
                client.send(b'U')
                time.sleep(delay)
            elif aY < -2:
                client.send(b'D')
                time.sleep(delay)

            if aX < -5:
                client.send(b'L')
                time.sleep(delay)
            elif aX > 5:
                client.send(b'R')
                time.sleep(delay)

            if aaZ < -200:
                client.send(b'L+S')
                time.sleep(delay)
            elif aaZ > 200:
                client.send(b'R+S')
                time.sleep(delay)
                    
    except KeyboardInterrupt:
        print("Cleanup")


if __name__ == '__main__':
    main()
