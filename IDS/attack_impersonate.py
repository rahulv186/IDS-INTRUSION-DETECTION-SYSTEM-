import paho.mqtt.client as mqtt
import ssl
import json
import time
import random

BROKER = "localhost"
PORT = 8883
CA = "/Users/rahul/mosquitto_certs/ca.crt"

client = mqtt.Client(client_id="impersonator")

client.tls_set(
    ca_certs=CA,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

client.connect(BROKER, PORT)
client.loop_start()   # keeps connection alive

def impersonate():
    payload={"device_id":"impersonator","temperature":random.randint(20,40),"client_id":"impersonator"}

    client.publish("home/temperature", json.dumps(payload))
    print("Message sent")

if __name__ == "__main__":
    while True:
        impersonate()
        time.sleep(5)