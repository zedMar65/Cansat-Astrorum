# imports
import time
import machine
from nmea_parser import parse_nmea_sentences
import dht
from libs.MPU6050 import init_mpu6050, get_mpu6050_data
#import libs.MPU6050

# magic
global true
global false
true = True
false = False

class SensorList:
    gy_91 = true
    radiation = false # don't change
    dust = false # don't change
    gps = true
    dht11 = true
    def __init__(self):
        return

class SENSOR:
    def __init__(self):
        self.init()
        return
    def update(self) -> str:
        return
    def init(self) -> None:
        return

class SENSOR_GY(SENSOR):
    def __init__(self, i2c):
        self.init(i2c)
        
    def update(self) -> str:
        try:
            #gyro = self.mpu.read_gyro_data()
            #accel = self.mpu.read_accel_data()
            #return {'gyro': gyro, 'Accel': accel}
            data = get_mpu6050_data(self.i2c)
            return data
        except Exception as e:
            print(f"Gyro error: {e}")
            return {'gyro': '', 'Accel': ''}
    
    def init(self, i2c) -> None:
        self.i2c = i2c
        print(self.i2c.scan())
        try:
            init_mpu6050(self.i2c)
        except Exception as e:
            print(f"Gyro init error: {e}")
        #self.mpu = libs.MPU6050.MPU6050(i2c)
        #self.mpu.wake()
        
class SENSOR_GPS(SENSOR):
    def __init__(self, gps_uart):
        self.init(gps_uart)
    
    def update(self) -> str:
        #gps_data = self.gps_reader.get_data()
        #return f"{gps_data.satellites}; {gps_data.has_fix}; {gps_data.latitude}; {gps_data.longitude}"
        
        if self.gps_uart.any():
            line = self.gps_uart.read()
            
            if line:
                # Attempt to decode the line using UTF-8
                decoded_line = "$"+"$".join(str(line).split('$')[1:])
                try:
                    return parse_nmea_sentences(decoded_line)
                except Exception as e:
                    print(f"Error in GPS: {e}")
                    return parse_nmea_sentences('')
                # If decoding fails, skip the line
                
        return parse_nmea_sentences('')
    
    def init(self, gps_uart) -> None:
        try:
            self.gps_uart = gps_uart
            #self.gps_reader = libs.gps_parser.GPSReader(gps_uart)
        except Exception as e:
            print(f"GPS init error: {e}")

class SENSOR_DHT11:
    def __init__(self, pin):
        self.init(pin)
    
    def update(self) -> str:
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()
            humi = self.sensor.humidity()
            return {'temperature': temp, 'humidity': humi}
        except Exception as e:
            print(f"dht11 error: {e}")
            return {'temperature': '', 'humidity': ''}
    
    def init(self, pin) -> None:
        self.sensor = dht.DHT11(pin)

class RADIO:
    radioChannel = None
    def __init__(self, uart):
        self.uart = uart

    def send(self, msg):
        try:
            self.uart.write((str(msg)+'\n').encode())
            return 0
        except Exception as e:
            print(f"Radio send error:{e}")
            return 1
        
    def read(self):
        try:
            msg = self.uart.read()
            return "You got a message: {msg}"
        except Exception as e:
            return f"Radio read error: {e}"