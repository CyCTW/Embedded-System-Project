import argparse
import socket
from gy801 import gy801
import time

parser = argparse.ArgumentParser()
parser.add_argument('ip')
parser.add_argument('port')
args = parser.parse_args()

def main():
    try:
        sensors = gy801()
        adxl345 = sensors.accel
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((args.ip, int(args.port)))

        while True:
            adxl345.getX()
            adxl345.getY()
            adxl345.getZ()

            msg = b'No'
            if adxl345.X < -8:
                msg = b'L+enter'
            elif adxl345.X < -3:
                msg = b'L'
            elif adxl345.X > 8:
                msg = b'R+enter'
            elif adxl345.X > 3:
                msg = b'R'
            elif adxl345.Y < -2.5:
                msg = b'D'
            elif adxl345.Y > 2.5:
                msg = b'U'
                
            client.send(msg)
            data = client.recv(1024)
            time.sleep(0.05)

                    
    except KeyboardInterrupt:
        print("Cleanup")


if __name__ == '__main__':
    main()
