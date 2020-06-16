import smbus

class IMU(object):

    def __init__(self):
        self.bus = smbus.SMBus(1)

    def write_byte(self, adr, value):
        self.bus.write_byte_data(self.ADDRESS, adr, value)
    
    def read_byte(self, adr):
        return self.bus.read_byte_data(self.ADDRESS, adr)

    def read_word(self, adr, rf = 1):
        # rf = 1 Little Endian Format, rf = 0 Big Endian Format
        low, high = self.read_byte(adr), self.read_byte(adr + 1)
        if rf != 1:
            low, high = high, low
        return (high << 8) + low

    def read_word_2c(self, adr, rf = 1):
        # rf = 1 Little Endian Format, rf = 0 Big Endian Format
        val = self.read_word(adr, rf)
        if (val & (1 << 16 - 1)):
            return val - (1 << 16)
        else:
            return val
