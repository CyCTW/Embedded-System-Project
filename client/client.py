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

        delay = 0.01
        while True:

            aaZ = sensor.getaaZ()
            if aaZ < -130:
                client.send(b'L+S')
                time.sleep(delay)
                continue
            elif aaZ > 130:
                client.send(b'R+S')
                time.sleep(delay)
                continue

            aY = sensor.getaY()
            if aY > 5:
                client.send(b'U')
                time.sleep(delay)
            elif aY < -2:
                client.send(b'D')
                time.sleep(delay)

            aX = sensor.getaX()
            if aX < -4:
                client.send(b'L')
                time.sleep(delay)
            elif aX > 4:
                client.send(b'R')
                time.sleep(delay)

                    
    except KeyboardInterrupt:
        print("Cleanup")


if __name__ == '__main__':
    main()
