import paho.mqtt.client as mqtt
import ssl
import json
import time
import random

BROKER = "localhost"
PORT = 8883
CA = "/Users/rahul/mosquitto_certs/ca.crt"

client = mqtt.Client(client_id="flooder")

client.tls_set(cert_reqs=mqtt.ssl.CERT_NONE)
client.tls_insecure_set(True)

client.connect(BROKER, PORT)  # keeps connection alive

def flood():
    for _ in range(20):
        payload={"device_id":"sensor1","temperature":random.randint(20,40),"client_id":"flooder"}
        client.publish("home/temperature", json.dumps(payload))
    print("Message sent")


flood()