import time
import requests
from xml_parser import parseXML
from concurrent.futures import ThreadPoolExecutor

from pubsub.pubsub import PubSub

##url for latest weather observations on meteo.arso.gov.si for all available places
url = 'https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_si_latest.xml'

def publisher():
    """
    To run execute the command "python publisher.py" in your cli
    
    Fetches latest weather observation data from meteo.arso.gov.si (url) for all available places every 30 seconds.
    After parsing the data it publishes the data for each place to its own channel (channel_name = place_name)

    Uses the ThreadPoolExecutor for concurrent publishing of messages on different channels (multithreading)

    Loop runs continously until interrupted with "Ctrl + C"
    """

    pubsub = PubSub()

    while True:
        response = requests.get(url)
        places_data = parseXML(response.content)
        with ThreadPoolExecutor(max_workers=5) as executor:
            for place in places_data:
                executor.submit(pubsub.publish, place, places_data[place])
        time.sleep(30)

if __name__ == '__main__':
    publisher()
