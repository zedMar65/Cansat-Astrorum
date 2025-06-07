from data import *
from sensors import *
import time

def initiate() -> None:
    SENSORS = SensorList()
    
    global data
    data = Data(SENSORS)

def main() -> None:
    On = True
    
    time.sleep(1)

    try:
        while On:
            data.update()

            print(data.get_data())
            
            time.sleep(1)

    except KeyboardInterrupt:
        On = False

initiate()
main()