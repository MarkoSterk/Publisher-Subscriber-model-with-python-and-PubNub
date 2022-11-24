import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

def parseXML(xml_object):
    """
    Parses the incomming xml_object and extracts all desired data
    Output is a dictionary with keys matching the places ('shortTitle' tag in xml) of the weather data
    Each key contains another dictionary with the weather data of the place
    (temperature, wind_speed, humidity)
    """
    data = xml_object.decode('utf-8')
    bs_content = bs(data, features="xml")
    places = bs_content.find_all('metData')

    places_data = {}
    for place in places:
        place_name = place.domain_shortTitle.text.strip().replace(' ', '').replace('Ž', 'Z').replace('-', '/').lower()
        places_data[place_name] = {}

        temp_field_value = place.t.text.lower().strip()
        places_data[place_name]['temperature'] = f'{temp_field_value} °C'

        wind_speed_value = place.ff_val_kmh.text.strip().lower()
        places_data[place_name]['wind_speed'] = f'{wind_speed_value} km/h'

        humidity_value = place.rh.text.strip().lower()
        places_data[place_name]['humidity'] = f'{humidity_value} %'
    
    return places_data


