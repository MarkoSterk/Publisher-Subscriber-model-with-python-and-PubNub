from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

import os
import random
import time

SUBSCRIBE_KEY = os.environ.get('SUBSCRIBE_KEY')
PUBLISH_KEY = os.environ.get('PUBLISH_KEY')

pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pnconfig.publish_key = PUBLISH_KEY

class Listener(SubscribeCallback):
    """
    Listener object
    Provides callback function "message" which is called each time a
    message is received
    """

    def message(self, pubnub, message_object) -> None:
        """
        Print received message to the cli
        """
        print(f'\n-- Channel: {message_object.channel} | {message_object.message}')



class PubSub():
    """
    Handles the publish/subscribe layer of the application
    """

    def __init__(self) -> None:
        self.pubnub = PubNub(pnconfig)
        self.pubnub.add_listener(Listener())
    
    def subscribe(self, channel: str) -> None:
        """
        Subscribes to provided channel
        """
        self.pubnub.subscribe().channels([channel]).execute()
    
    def unsubscribe(self, channel: str) -> None:
        """
        Unsubscribes from provided channel
        """
        self.pubnub.unsubscribe().channels([channel]).execute()

    def unsubscribe_all(self) -> None:
        """
        Unsubscribes from all channels
        """
        self.pubnub.unsubscribe_all()

    def publish(self, channel: str, message) -> None:
        """
        Publish the message object to the channel
        """
        sleep_time = random.uniform(0.5, 1.0)
        time.sleep(sleep_time)
        self.pubnub.publish().channel(channel).message(message).sync()


