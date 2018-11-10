import paho.mqtt.client as mqtt
import os
import time
import json
import random
import sys
def dht12():
    toSend = dict()
    toSend["temp"] = random.uniform(30,50)
    toSend["humidity"] = random.uniform(10,40)
    return json.dumps(toSend)
def button():
    toSend = dict()
    toSend["value"] = bool(random.getrandbits(1))
    return json.dumps(toSend)

IP = os.environ["MQTTIP"]
PORT = int(os.environ["MQTTPORT"])
TOPIC = os.environ["TOPIC"]
TYPE = os.environ["TYPE"]
client = mqtt.Client()

client.connect(IP, PORT, 60)
function = None
if TYPE == "dht12":
    function = dht12
elif TYPE == "button":
    function = button
else:
    print("Unsupported type -", TYPE)
    sys.exit(1)

while True:
    dumped = function()
    print(dumped)
    client.publish(TOPIC, dumped)
    time.sleep(0.5)
