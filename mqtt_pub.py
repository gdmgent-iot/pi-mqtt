import sys
import time
import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

if client.connect("mqtt.eclipseprojects.io", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

try:
    while True:
        client.publish("test_topic", "Hi, paho mqtt client works fine!", 0)
        time.sleep(1)
finally:
    client.disconnect()