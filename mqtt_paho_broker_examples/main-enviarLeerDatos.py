from paho.mqtt import client as mqtt_client
import json
import random
import time

BROKER="broker.emqx.io"
PORT=1883
TOPIC="BMP180"

CLIENT_ID="client-incendio-dron-{id}".format(id=random.randint(0,1000))
USERNAME=""
PASSWORD=""
FLAG_CONNECTED=0

def on_connect(client,userdata,flags,rc):
    global FLAG_CONNECTED
    if rc==0:
        FLAG_CONNECTED=1
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

def publish(client):
    msg_count=0
    while True:
        msg_dict={
            'msg': msg_count
        }
        msg=json.dumps(msg_dict)
        result=client.publish(TOPIC,msg)
        status=result[0]
        if status==0:
            print("Enviar `{msg}` al TOPIC `{topic}`".format(msg=msg, topic=TOPIC))
        else:
            print("Error al enviar mensaje por Topic `{TOPIC}`".format(topic=TOPIC))
        msg_count+=1
        time.sleep(5)

def run():
    client=connect_mqtt()
    client.loop_start()
    time.sleep(5)
    if FLAG_CONNECTED:
        publish(client)
    else:
        client.loop_stop()

if __name__=='__main__':
    run()