from module.IMU import IMU
from tqdm import tqdm

ADXL345_ADDRESS                 = 0x53
ADXL345_OFSX                    = 0x1E
ADXL345_OFSY                    = 0x1F
ADXL345_OFSZ                    = 0x20
ADXL345_BW_RATE                 = 0x2C
ADXL345_POWER_CTL               = 0x2D
ADXL345_POWER_CTL_MEASURE       = 0x08
ADXL345_DATA_FORMAT             = 0x31
ADXL345_DATA_FORMAT_FULL_RES    = 0x08
ADXL345_DATAX0                  = 0x32
ADXL345_DATAY0                  = 0x34
ADXL345_DATAZ0                  = 0x36
ADXL345_SCALE_MULTIPLIER        = 0.00390625
EARTH_GRAVITY_MS2               = 9.80665

class ADXL345(IMU):

    def __init__(self):
        super().__init__()
        self.ADDRESS = ADXL345_ADDRESS
        self.write_byte(ADXL345_POWER_CTL, ADXL345_POWER_CTL_MEASURE)
        self.write_byte(ADXL345_DATA_FORMAT, ADXL345_DATA_FORMAT_FULL_RES)

    def __getRawX(self):
        return self.read_word_2c(ADXL345_DATAX0)

    def __getRawY(self):
        return self.read_word_2c(ADXL345_DATAY0)

    def __getRawZ(self):
        return self.read_word_2c(ADXL345_DATAZ0)

    def getXg(self):
        return self.__getRawX() * ADXL345_SCALE_MULTIPLIER

    def getYg(self):
        return self.__getRawY() * ADXL345_SCALE_MULTIPLIER

    def getZg(self):
        return self.__getRawZ() * ADXL345_SCALE_MULTIPLIER

    def getX(self):
        return self.getXg() * EARTH_GRAVITY_MS2

    def getY(self):
        return self.getYg() * EARTH_GRAVITY_MS2

    def getZ(self):
        return self.getZg() * EARTH_GRAVITY_MS2

    def calibrate(self, n = 10000):
        print ("Calibrating ADXL345...")
        X, Y, Z = 0, 0, 0
        rX, rY, rZ = 0, 0, 256
        
        for i in tqdm(range(n)):
            X += self.__getRawX()
            Y += self.__getRawY()
            Z += self.__getRawZ()

        X, Y, Z = round(X / n), round(Y / n), round(Z / n)
        if Z < 0:
            rZ = -rZ

        self.write_byte(ADXL345_OFSX, -round((X - rX) / 4))
        self.write_byte(ADXL345_OFSY, -round((Y - rY) / 4))
        self.write_byte(ADXL345_OFSZ, -round((Z - rZ) / 4))
