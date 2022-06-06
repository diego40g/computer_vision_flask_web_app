from paho.mqtt import client as mqtt_client
import random
import time

BROKER="broker.emqx.io"
PORT=1883
TOPIC="BMP180"

CLIENT_ID="client-incendio-dron-{id}".format(id=random.randint(0,1000))
USERNAME=""
PASSWORD=""

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Conectando a MQTT Broker!!!")
        client.subscribe(TOPIC)
    else:
        print("Fallo al conectar, error en {rc}".format(rc=rc),)

def on_message(client,userdata,msg):
    print("Recibido `{payload}` desde `{topic}` topic".format(
        payload=msg.payload.decode(), topic=msg.topic
    ))

def connect_mqtt():
    client=mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME,PASSWORD)
    client.on_connect=on_connect
    client.on_message=on_message
    client.connect(BROKER,PORT)
    return client

def run():
    client=connect_mqtt()
    client.loop_forever()


if __name__=='__main__':
    run()    
