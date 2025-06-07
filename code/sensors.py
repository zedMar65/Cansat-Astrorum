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
    name = "sensor"

    def __init__(self):
        return
    def update(self) -> dict:
        return {}
    def init(self) -> None:
        return

class SENSOR_GY(SENSOR):
    name = "gy91"

    def __init__(self):
        return
        
    def update(self) -> dict:
        return {}
    
    def init(self) -> None:
        return

        
class SENSOR_GPS(SENSOR):
    name = "gps"

    def __init__(self):
        return
    
    def update(self) -> dict:
        return {}

    def init(self) -> None:
        return

class SENSOR_DHT11:
    name = "dht11"

    def __init__(self):
        return
    
    def update(self) -> dict:
        return {}
    
    def init(self) -> None:
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