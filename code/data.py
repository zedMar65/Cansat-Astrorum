import json
from sensors import *

def to_json(obj):
    return ujson.dumps(obj)

class Data:
    sensors = {}
    data = {}
    radio = None
    
    def __init__(self, sensorList, radioChannel):
        if sensorList.gy_91:
            self.sensors["sensor_gy"] = SENSOR_GY()
        if sensorList.radiation:
            self.sensors["sensor_radiation"] = SENSOR_RADIATION()
        if sensorList.dust:
            self.sensors["sensor_dust"] = SENSOR_DUST()
        if sensorList.gps:
            self.sensors["sensor_gps"] = SENSOR_GPS()
        
        self.radio = RADIO(radioChannel)
        return
    
    def update(self) -> None:
        keys = self.sensors.keys()
        for sensor in keys:
            self.data[sensor] = self.sensors[sensor].update()
        return
    
    def get_data(self) -> str:
        return self.data
    
    def re_init(self) -> None:
        sensorList = sensors.values()
        for sensor in sensorList:
            sensor.__init__()
        return