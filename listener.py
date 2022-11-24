import sys
from pubsub.pubsub import PubSub


def listener():
    """
    To run execute the command "python listener.py place_name" in your cli

    Takes name of the channel to subscribe to from the cli with sys.argv[1]
    
    Available weather channels from publisher.py:
    'celje', 'cerklje/airport', 'crnomelj', 'katarina', 'kocevje', 'kredarica',
    'lesce', 'lisca', 'ljubljana/bezigrad', 'ljubljana/airport', 'mariborairport',
    'murskasobota', 'novagorica', 'novomesto', 'portoroz/airport', 'postojna', 
    'ratece', 'slovenjgradec', 'vogel', 'vojsko'
    """

    def error_message(msg):
        return f"""
            {msg}
            Available weather channels are:
            'celje', 'cerklje/airport', 'crnomelj', 'katarina', 'kocevje', 'kredarica',
            'lesce', 'lisca', 'ljubljana/bezigrad', 'ljubljana/airport', 'mariborairport',
            'murskasobota', 'novagorica', 'novomesto', 'portoroz/airport', 'postojna', 
            'ratece', 'slovenjgradec', 'vogel', 'vojsko'
        """

    if len(sys.argv) == 1: print(error_message('Please provide a channel to subscribe to.'))
    elif len(sys.argv) > 2: print(error_message('Please provide just one channel to subscribe to.'))
    else:
        pubsub = PubSub()
        channel = sys.argv[1]
        print(f'Successfully subscribed to channel: {channel}')
        pubsub.subscribe(channel)

if __name__ == '__main__':
    listener()