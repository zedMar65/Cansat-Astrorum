# gps_parser.py - A simple library for parsing NMEA GPS data
# For use with UART GPS modules on Raspberry Pi Pico

import time

class GPSData:
    """Class to store GPS data with easy attribute access"""
    def __init__(self):
        self.has_fix = False
        self.latitude = 0.0
        self.longitude = 0.0
        self.speed_knots = 0.0
        self.time = ""
        self.date = ""
        self.satellites = 0
        self.altitude = 0.0
        self.hdop = 0.0  # Horizontal Dilution of Precision
        self.pdop = 0.0  # Position Dilution of Precision
        self.vdop = 0.0  # Vertical Dilution of Precision

# This would replace the existing GPSReader class in your gps_parser.py file

class GPSReader:
    """Class to handle GPS reading with non-blocking updates when getting data"""
    def __init__(self, uart):
        self.uart = uart
        self.message_buffer = ""
        self.last_data_time = time.ticks_ms()
        self.timeout_ms = 500  # 500ms timeout between message parts
        self.current_data = GPSData()
        self.has_new_data = False
    
    def update(self):
        """Check for new GPS data and process it - non-blocking version"""
        self.has_new_data = False
        current_time = time.ticks_ms()
        
        # Check if timeout occurred with data in buffer
        if time.ticks_diff(current_time, self.last_data_time) > self.timeout_ms and self.message_buffer:
            self._process_buffer()
            self.has_new_data = True
        
        # Check if new data is available - only read what's currently available
        bytes_available = self.uart.any()
        if bytes_available > 0:
            try:
                # Read ONLY the currently available data - this is the key non-blocking change
                line = self.uart.read()
                
                data = "$"+"$".join(str(line).split('$')[1:])
                
                print(f"Data: {data}")
                
                # If buffer is empty or we recently received data, append to buffer
                
                # If timeout occurred, process the old buffer first
                self._process_buffer()
                # Then start a new buffer
                self.message_buffer = data
                self.has_new_data = True
                
                # Update last data time
                self.last_data_time = current_time
            except Exception as e:
                print(f"Error reading GPS data: {e}")
        
        return self.has_new_data
    
    def get_data(self):
        """
        Get the current GPS data.
        Automatically updates before returning the data.
        
        Returns:
            GPSData: The current GPS data object with the most recent reading
        """
        self.update()
        return self.current_data
    
    def _process_buffer(self):
        """Process the complete message in buffer"""
        if not self.message_buffer:
            return
        
        self.current_data = _process_nmea_data(self.message_buffer)
        self.message_buffer = ""
    
    # Convenience properties for direct access to GPS data
    @property
    def latitude(self):
        """Get the current latitude"""
        self.update()
        return self.current_data.latitude
    
    @property
    def longitude(self):
        """Get the current longitude"""
        self.update()
        return self.current_data.longitude
    
    @property
    def altitude(self):
        """Get the current altitude"""
        self.update()
        return self.current_data.altitude
    
    @property
    def has_fix(self):
        """Get the current fix status"""
        self.update()
        return self.current_data.has_fix
    
    @property
    def satellites(self):
        """Get the current number of satellites"""
        self.update()
        return self.current_data.satellites
    
    @property
    def speed(self):
        """Get the current speed in knots"""
        self.update()
        return self.current_data.speed_knots
    
    @property
    def time(self):
        """Get the current GPS time"""
        self.update()
        return self.current_data.time
    
    @property
    def date(self):
        """Get the current GPS date"""
        self.update()
        return self.current_data.date

# For backward compatibility
def parse_gps_data(nmea_chunk):
    """Legacy function to parse GPS data (for compatibility)"""
    return _process_nmea_data(nmea_chunk)

def _process_nmea_data(nmea_data):
    """Process a complete NMEA data string"""
    # Initialize data class
    gps_data = GPSData()
    
    # Split the chunk into individual NMEA sentences
    sentences = nmea_data.strip().split('$')
    
    # Process each sentence
    for sentence in sentences:
        if not sentence:
            continue
            
        # Add the $ back for proper format
        sentence = '$' + sentence.strip()
        
        # Parse different sentence types
        if sentence.startswith('$GPRMC'):
            _parse_rmc(sentence, gps_data)
        elif sentence.startswith('$GPGGA'):
            _parse_gga(sentence, gps_data)
        elif sentence.startswith('$GPGSA'):
            _parse_gsa(sentence, gps_data)
    
    return gps_data

def _parse_rmc(sentence, gps_data):
    """Parse RMC sentence for time, date, location, and speed"""
    
    # Split the sentence into parts
    parts = sentence.split(',')
    
    if len(parts) < 12:
        return
    
    # Check if we have a fix
    if parts[2] == 'A':
        gps_data.has_fix = True
    else:
        gps_data.has_fix = False
        # Don't return here, continue to extract time and date
    
    # Extract time (format: HHMMSS.SS) with error handling
    if parts[1] and len(parts[1]) >= 6:
        try:
            hour = parts[1][0:2]
            minute = parts[1][2:4]
            second = parts[1][4:]
            gps_data.time = f"{hour}:{minute}:{second}"
        except (ValueError, IndexError):
            # Keep the existing time value if parsing fails
            pass
    
    # Extract date (format: DDMMYY) with error handling
    if parts[9] and len(parts[9]) >= 6:
        try:
            day = parts[9][0:2]
            month = parts[9][2:4]
            year = "20" + parts[9][4:6]  # Assuming we're in the 2000s
            gps_data.date = f"{day}/{month}/{year}"
        except (ValueError, IndexError):
            # Keep the existing date value if parsing fails
            pass
    
    # Only extract position and speed if we have a valid fix
    if gps_data.has_fix:
        # Extract latitude and longitude with sign based on direction
        if parts[3] and parts[5]:
            try:
                # Latitude
                lat_deg = float(parts[3][0:2])
                lat_min = float(parts[3][2:])
                lat_decimal = lat_deg + (lat_min / 60)
                
                # Apply sign based on direction (N is positive, S is negative)
                if parts[4] == 'S':
                    lat_decimal = -lat_decimal
                gps_data.latitude = lat_decimal
                
                # Longitude
                lon_deg = float(parts[5][0:3])
                lon_min = float(parts[5][3:])
                lon_decimal = lon_deg + (lon_min / 60)
                
                # Apply sign based on direction (E is positive, W is negative)
                if parts[6] == 'W':
                    lon_decimal = -lon_decimal
                gps_data.longitude = lon_decimal
            except (ValueError, IndexError):
                # If parsing fails, don't update coordinates
                pass
        
        # Extract speed in knots
        if parts[7]:
            try:
                gps_data.speed_knots = float(parts[7])
            except ValueError:
                gps_data.speed_knots = 0.0

def _parse_gga(sentence, gps_data):
    """Parse GGA sentence for satellites, altitude, and HDOP"""
    
    parts = sentence.split(',')
    
    if len(parts) < 15:
        return
    
    # Extract number of satellites
    if parts[7]:
        try:
            gps_data.satellites = int(parts[7])
        except ValueError:
            gps_data.satellites = 0
    
    # Extract HDOP (Horizontal Dilution of Precision)
    if parts[8]:
        try:
            gps_data.hdop = float(parts[8])
        except ValueError:
            gps_data.hdop = 0.0
    
    # Extract altitude
    if parts[9] and parts[10] == 'M':
        try:
            gps_data.altitude = float(parts[9])
        except ValueError:
            gps_data.altitude = 0.0

def _parse_gsa(sentence, gps_data):
    """Parse GSA sentence for PDOP, HDOP, and VDOP"""
    
    parts = sentence.split(',')
    
    if len(parts) < 18:
        return
    
    # Extract PDOP (Position Dilution of Precision)
    if parts[15]:
        try:
            gps_data.pdop = float(parts[15])
        except ValueError:
            gps_data.pdop = 0.0
            
    # Extract HDOP (Horizontal Dilution of Precision)
    if parts[16]:
        try:
            gps_data.hdop = float(parts[16])
        except ValueError:
            pass  # Keep existing value if we can't parse this one
    
    # Extract VDOP (Vertical Dilution of Precision)
    if parts[17].split('*')[0]:  # Remove checksum part
        try:
            gps_data.vdop = float(parts[17].split('*')[0])
        except ValueError:
            gps_data.vdop = 0.0