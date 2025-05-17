global true
global false
true = True
false = False


class SensorList:
    gy_91 = true
    radiation = false
    dust = false
    gps = false
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
    def __init__(self):
        super().__init__()
    def update(self) -> str:
        print("gy_update")
        return ""
    def init(self) -> None:
        print("gy_init")

class RADIO:
    radioChannel = None
    def __init__(self, radioChannel):
        self.radioChannel = radioChannel