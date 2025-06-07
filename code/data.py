import json
from sensors import *

def to_json(obj):
    return ujson.dumps(obj)

def init_sensor(sensor):
    try:
        sensor.init()
        return True
    except Exception as e:
        print(f"{sensor.name} init failed: {e}")
        return False

class Data:
    sensors = []
    data = {}
    radio = None
    
    def __init__(self, sensorList):
        self.sensors = [ # List all coded sensors here
            
        ]
        
        self.sensors = [sensor for sensor in self.sensors if sensor is not None and init_sensor(sensor)]

        return
    
    def update(self) -> None:
        for sensor in self.sensors:
            self.data[sensor.name] = sensor.update()
        return
    
    def get_data(self) -> dict:
        return self.data
    
    def re_init(self) -> None:
        for sensor in self.sensors:
            sensor.init()
        return
