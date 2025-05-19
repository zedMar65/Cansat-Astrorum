from data import *
from sensors import *
import time

def initiate() -> None:
    SENSORS = SensorList()

    global data
    data = Data(SENSORS)

def main() -> None:
    #data.update()
    
    On = True
    
    time.sleep(1)
    
    file=open("log.txt","w")
    try:
        while On:
            data.update()
            file.write(str(data.get_data())+'\n')
            file.flush()
            if data.radio:
                data.radio.send(data.get_data())
            else:
                print(data.get_data())
            time.sleep(1)
            
    except KeyboardInterrupt:
        On = False
        
    #except Exception as e:
    #    print(f"Error in main: {e}")
            
    file.close()
    

initiate()
main()