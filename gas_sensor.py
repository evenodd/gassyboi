import time
import board
import busio
import adafruit_sgp30

class GasSensor:
    def __init__(self) :
        self.i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
          self.sgp30 = adafruit_sgp30.Adafruit_SGP30(self.i2c)
          print("SGP30 serial #", [hex(i) for i in self.sgp30.serial])

    def getData(self) :
        return self.sgp30.co2eq, self.sgp30.tvoc
