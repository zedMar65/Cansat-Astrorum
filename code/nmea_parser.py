def nmea_to_decimal(coord_str, direction):
    """
    Converts NMEA coordinate format (ddmm.mmmm) to decimal degrees.

    Parameters:
    - coord_str (str): Coordinate string in NMEA format.
    - direction (str): Direction character ('N', 'S', 'E', 'W').

    Returns:
    - float: Coordinate in decimal degrees.
    """
    if not coord_str or not direction:
        raise ValueError("Invalid coordinate or direction.")

    # Convert string to float
    coord = float(coord_str)

    # Extract degrees and minutes
    degrees = int(coord) // 100
    minutes = coord - (degrees * 100)

    # Convert to decimal degrees
    decimal_degrees = degrees + (minutes / 60)

    # Apply negative sign for South and West
    if direction.upper() in ['S', 'W']:
        decimal_degrees *= -1

    return decimal_degrees


def parse_nmea_sentences(nmea_data):
    """
    Parses NMEA sentences from a string and returns a list of formatted GPS information.

    :param nmea_data: String containing NMEA sentences separated by newline characters.
    :return: List of formatted strings with GPS information.
    """
    results = {'time': '', 'latitude': '', 'longitude': '', 'altitude': '', 'speed': ''}
    
    lines = nmea_data.strip().splitlines()
    
    if lines == '':
        return results

    for line in lines:
        line = line.strip()
        if not line.startswith('$'):
            continue  # Skip lines that are not NMEA sentences

        # Remove checksum and split the sentence
        if '*' in line:
            line = line.split('*')[0]
        parts = line.split(',')

        sentence_type = parts[0][3:]

        if sentence_type == 'GGA':
            # Global Positioning System Fix Data
            time_utc = parts[1]
            lat = parts[2]
            lat_dir = parts[3]
            lon = parts[4]
            lon_dir = parts[5]
            fix_quality = parts[6]
            num_satellites = parts[7]
            altitude = parts[9]
            altitude_units = parts[10]
            
            results['time'] = time_utc
            results['latitude'] = nmea_to_decimal(lat, lat_dir)
            results['longitude'] = nmea_to_decimal(lon, lon_dir)
            results['altitude'] = altitude

        elif sentence_type == 'RMC':
            # Recommended Minimum Specific GPS/Transit Data
            time_utc = parts[1]
            status = parts[2]
            lat = parts[3]
            lat_dir = parts[4]
            lon = parts[5]
            lon_dir = parts[6]
            speed = parts[7]
            date = parts[9]
            
            results['time'] = time_utc
            results['latitude'] = nmea_to_decimal(lat, lat_dir)
            results['longitude'] = nmea_to_decimal(lon, lon_dir)
            results['speed'] = speed

        elif sentence_type == 'GLL':
            # Geographic Position – Latitude/Longitude
            lat = parts[1]
            lat_dir = parts[2]
            lon = parts[3]
            lon_dir = parts[4]
            time_utc = parts[5]
            status = parts[6]
            
            results['time'] = time_utc
            results['latitude'] = nmea_to_decimal(lat, lat_dir)
            results['longitude'] = nmea_to_decimal(lon, lon_dir)

        else:
            results['time'] = ""

    return results
