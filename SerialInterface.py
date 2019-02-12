import serial

class SerialInterface:
    def __init__(self):
        self.ser

    def findUSBPort(self):
        try:
            self.ser = serial.Serial('/dev/ttyUSB0')
        except Exception:
            print()
