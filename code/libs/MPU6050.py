# custom lib mainly by chatgpt

from machine import Pin, I2C
import utime
"""
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
TEMP_OUT_H = 0x41
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
"""

ADXL345_ADDR = 0x53
ITG3205_ADDR = 0x68

DATA_FORMAT = 0x31

def twos_complement(val):
    return val - 65536 if val > 32767 else val

 
def init_mpu6050(i2c, address=0x68):
    i2c.writeto_mem(ADXL345_ADDR, 0x2D, b'\x08') # this don't work, because i2c is empty
    #i2c.writeto_mem(ADXL345_ADDR, DATA_FORMAT, b'\x08') # untested chatgpt suggestion
    
    i2c.writeto_mem(ITG3205_ADDR, 0x3E, b'\x00')
    i2c.writeto_mem(ITG3205_ADDR, 0x16, b'\x18')
    
    #i2c.writeto_mem(address, PWR_MGMT_1, b'\x00')
    #utime.sleep_ms(100)
    #i2c.writeto_mem(address, SMPLRT_DIV, b'\x07')
    #i2c.writeto_mem(address, CONFIG, b'\x00')
    #i2c.writeto_mem(address, GYRO_CONFIG, b'\x00')
    #i2c.writeto_mem(address, ACCEL_CONFIG, b'\x00')
"""
def read_raw_data(i2c, addr, address=0x68):
    high = i2c.readfrom_mem(address, addr, 1)[0]
    low = i2c.readfrom_mem(address, addr + 1, 1)[0]
    value = high << 8 | low
    if value > 32768:
        value = value - 65536
    return value
"""
def get_mpu6050_data(i2c):
    """temp = read_raw_data(i2c, TEMP_OUT_H) / 340.0 + 36.53
    accel_x = read_raw_data(i2c, ACCEL_XOUT_H) / 16384.0
    accel_y = read_raw_data(i2c, ACCEL_XOUT_H + 2) / 16384.0
    accel_z = read_raw_data(i2c, ACCEL_XOUT_H + 4) / 16384.0
    gyro_x = read_raw_data(i2c, GYRO_XOUT_H) / 131.0
    gyro_y = read_raw_data(i2c, GYRO_XOUT_H + 2) / 131.0
    gyro_z = read_raw_data(i2c, GYRO_XOUT_H + 4) / 131.0
    """
    data = i2c.readfrom_mem(ADXL345_ADDR, 0x32, 6)
    accel_x = twos_complement(int.from_bytes(data[0:2], 'little'))
    accel_y = twos_complement(int.from_bytes(data[2:4], 'little'))
    accel_z = twos_complement(int.from_bytes(data[4:6], 'little'))
    
    data = i2c.readfrom_mem(ITG3205_ADDR, 0x1D, 6)
    gyro_x = twos_complement(int.from_bytes(data[0:2], 'big'))
    gyro_y = twos_complement(int.from_bytes(data[2:4], 'big'))
    gyro_z = twos_complement(int.from_bytes(data[4:6], 'big'))
    
    temp = 0
    
    return {
        #'temp': temp,
        'accel': {
            'x': accel_x,
            'y': accel_y,
            'z': accel_z,
        },
        'gyro': {
            'x': gyro_x,
            'y': gyro_y,
            'z': gyro_z,
        }
    }