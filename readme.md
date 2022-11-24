# Publish/Subscribe model implemented with PubNub

Developed with Python version 3.11.

## Installation
Create and run a virtual environment with (example)
```
python3.11 -m venv venv
source venv/bin/activate
```
and install all requirements with
```
pip install -r requirements.txt
```

## listener.py
The listener.py file implements a subscriber on PubSub. It takes a
channel name as input it runtime of the script as shown below:
```
python listener.py <place_name>
```
Available weather channels from publisher.py:
'celje', 'cerklje/airport', 'crnomelj', 'katarina', 'kocevje', 'kredarica',
'lesce', 'lisca', 'ljubljana/bezigrad', 'ljubljana/airport', 'mariborairport',
'murskasobota', 'novagorica', 'novomesto', 'portoroz/airport', 'postojna', 
'ratece', 'slovenjgradec', 'vogel', 'vojsko'

## publisher.py
The publisher.py file implements the publisher on the PubSub network. 
It starts an infinite loop where the publisher fetches and parses weather data from
meteo.arso.gov.si (Slovenian weather agency) for all available places every 30 seconds.

It than publishes the data for each place to its own channel (channel_name = place_name)

The publisher.py script can be executed with:
```
python publisher.py
```

The script can ofcourse be modified to work with any provided data (xml format)

## PubSub class in /pubsub/pubsub.py
Implements all the logic for subscribing/publishing to the PubNub network
It requires an existing PubNub account and running PubNub app.
After you have successfully registered an account on www.pubnub.com and created the app
use the PUBLISH_KEY and SUBSCRIBE_KEY of the app and set them as environmental variables
in the 'venv/bin/activate' file with:
```
export PUBLISH_KEY="your-publish-key"
export SUBSCRIBE_KEY="your-subscribe-key"
```
Don't forget to unset the variables in the deactivation section of the 'venv/bin/activate' file with:
```
unset PUBLISH_KEY
unset SUBSCRIBE_KEY
```

