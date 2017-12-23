import paho.mqtt.client as mqtt
print dir (mqtt)

import time
from datetime import datetime
from math import radians
from pytz import timezone

newReceivedMQTTdata=-1

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("myNewRan")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global newReceivedMQTTdata
    if __name__ == '__main__':
        print(msg.topic+" "+str(msg.payload))
    newReceivedMQTTdata=(datetime.now(tz=timezone('Europe/Moscow')).minute+datetime.now(tz=timezone('Europe/Moscow')).second/60.+datetime.now(tz=timezone('Europe/Moscow')).microsecond/1000000./60.,int(msg.payload))
    # if __name__ == '__main__':
        # print newReceivedMQTTdata

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

# client.loop_forever()
print("start listening to ..myNewRan..")
client.loop_start()

if __name__=='__main__':
    print("will wait for 10.5 sec ")
    time.sleep(10.5)
    client.loop_stop()
    print("finished listening")