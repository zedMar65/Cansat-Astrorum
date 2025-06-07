import json
from sensors import *
from machine import Pin, SPI, SoftSPI, UART, SoftI2C, I2C
import time

def to_json(obj):
    return ujson.dumps(obj)

class Data:
    sensors = {}
    data = {}
    radio = None
    
    def __init__(self, sensorList):        
        if sensorList.gy_91:
            try:
                self.sensors["sensor_gy"] = SENSOR_GY(I2C(0, sda=Pin(14), scl=Pin(15)))
            except Exception as e:
                print(f"GY fail as expected: {e}")
        if sensorList.radiation:
            self.sensors["sensor_radiation"] = SENSOR_RADIATION()
        if sensorList.dust:
            self.sensors["sensor_dust"] = SENSOR_DUST()
        if sensorList.gps:
            self.sensors["sensor_gps"] = SENSOR_GPS(UART(0, baudrate=115200, tx=Pin(12), rx=Pin(13)))
        if sensorList.dht11:
            self.sensors["sensor_dht11"] = SENSOR_DHT11(Pin(6, Pin.OUT, Pin.PULL_DOWN))
        
        self.radio = RADIO(
            UART(1, baudrate=57600, tx=Pin(4), rx=Pin(5)) # uart
        )
        
        return
    
    def update(self) -> None:
        keys = self.sensors.keys()
        for sensor in keys:
            self.data[sensor] = self.sensors[sensor].update()
        return
    
    def get_data(self) -> dict:
        return self.data
    
    def re_init(self) -> None:
        sensorList = sensors.values()
        for sensor in sensorList:
            sensor.__init__()
        return
