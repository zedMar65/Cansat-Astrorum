# imports
import time
import machine
import dht

# magic
global true
global false
true = True
false = False

class SensorList:
    gy_91 = true
    radiation = false
    dust = false
    gps = true
    dht11 = true
    def __init__(self):
        return

class SENSOR:
    def __init__(self):
        self.init()
        return
    def update(self) -> dict:
        return {}
    def init(self) -> None:
        return

class SENSOR_GY(SENSOR):
    def __init__(self, i2c):
        self.init(i2c)
        
    def update(self) -> dict:
        return {}
    
    def init(self, i2c) -> None:
        return

        
class SENSOR_GPS(SENSOR):
    def __init__(self, gps_uart):
        self.init(gps_uart)
    
    def update(self) -> dict:
        return {}

    def init(self, gps_uart) -> None:
        return

class SENSOR_DHT11:
    def __init__(self, pin):
        self.init(pin)
    
    def update(self) -> dict:
        return {}
    
    def init(self, pin) -> None:
        return

class RADIO:
    def __init__(self, radio_uart):
        self.radio_uart = radio_uart

    def send(self, msg):
        try:
            print(f"send: {str(msg)}")
            self.radio_uart.write((str(msg)+'\n').encode())
            return 0
        except Exception as e:
            print(f"Radio send error:{e}")
            return 1
        
    def read(self):
        try:
            if self.radio_uart.any():
                msg = self.radio_uart.read()
                return f"You got a message: {msg.decode()}"
            else:
                return ""
        except Exception as e:
            return f"Radio read error: {e}"