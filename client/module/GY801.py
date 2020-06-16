from module.ADXL345 import ADXL345
from module.L3G4200D import L3G4200D

class GY801(object):

    def __init__(self):
        self.accel  = ADXL345()
        self.gyro   = L3G4200D()

    def getaXg(self):
        return self.accel.getXg()

    def getaYg(self):
        return self.accel.getYg()

    def getaZg(self):
        return self.accel.getZg()

    def getaX(self):
        return self.accel.getX()

    def getaY(self):
        return self.accel.getY()

    def getaZ(self):
        return self.accel.getZ()

    def getaaX(self):
        return self.gyro.getX()

    def getaaY(self):
        return self.gyro.getY()

    def getaaZ(self):
        return self.gyro.getZ()
