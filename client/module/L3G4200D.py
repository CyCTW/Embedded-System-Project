from module.IMU import IMU

L3G4200D_ADDRESS                = 0x69
L3G4200D_CTRL_REG1              = 0x20
L3G4200D_CTRL_REG4              = 0x23
L3G4200D_OUT_X_L                = 0x28
L3G4200D_OUT_Y_L                = 0x2A
L3G4200D_OUT_Z_L                = 0x2C
L3G4200D_SCALE_MULTIPLIER_STD   = 0.00875

class L3G4200D(IMU):

    def __init__(self):
        super().__init__()
        self.ADDRESS = L3G4200D_ADDRESS
        self.write_byte(L3G4200D_CTRL_REG1, 0x0F)
        self.write_byte(L3G4200D_CTRL_REG4, 0x80)

    def __getRawX(self):
        return self.read_word_2c(L3G4200D_OUT_X_L)

    def __getRawY(self):
        return self.read_word_2c(L3G4200D_OUT_Y_L)

    def __getRawZ(self):
        return self.read_word_2c(L3G4200D_OUT_Z_L)

    def __get_scale_multiplier(self):
        return 2 ** (self.read_byte(L3G4200D_CTRL_REG4) & 0x30 >> 4) * L3G4200D_SCALE_MULTIPLIER_STD

    def getX(self):
        return self.__getRawX() * self.__get_scale_multiplier()

    def getY(self):
        return self.__getRawY() * self.__get_scale_multiplier()

    def getZ(self):
        return self.__getRawZ() * self.__get_scale_multiplier()
