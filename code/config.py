"""

Config lib for globally accessable data contains:
* Error codes
* Print status codes
* Changing variables

"""

# For quick access global vars, that might change
class Vars:
    LOG_ID = None
    HARDWARE_LOG_PATH = None
    CURRENT_TIME = None

# For quick access constants
class Consts:
    # logging options uses bitmap by default
    UART_PRINT = 0x01
    WIFI_PRINT = 0x02
    RADIO_PRINT = 0x04
    STORAGE_PRINT = 0x08
    LOG = UART_PRINT | WIFI_PRINT | RADIO_PRINT | STORAGE_PRINT
    FALLBACK1 = RADIO_PRINT | STORAGE_PRINT | UART_PRINT
    FALLBACK2 = RADIO_PRINT | UART_PRINT
    FALLBACK3 = RADIO_PRINT | STORAGE_PRINT
    
    # Logging status levels
    # Data must be sent as a valid json format as per Sensors.Data
    ERROR = "E"
    INFO = "I"
    DATA = "D"


# For quick access Error codes
class Errors:
    custom_error_message=None
