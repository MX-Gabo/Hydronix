import json
import paho.mqtt.client as mqtt
import time


class MQTTManager:

    def __init__(self):

        # ==================================
        # BROKER MQTT
        # ==================================

        self.BROKER = "broker.emqx.io"

        self.PORT = 1883

        # ==================================
        # CLIENTE MQTT
        # ==================================

        self.client = mqtt.Client()

        # ==================================
        # CALLBACKS
        # ==================================

        self.client.on_connect = self.on_connect

        self.client.on_message = self.on_message

        self.client.on_disconnect = self.on_disconnect

        # ==================================
        # ESTADO ESP32
        # ==================================

        self.esp32_online = False

        self.last_pong = 0

        # ==================================
        # DATOS SENSORES
        # ==================================

        self.temperatura = "0"

        self.humedad_aire = "0"

        self.humedad_suelo1 = "0"

        self.humedad_suelo2 = "0"

    # ======================================
    # CONECTAR
    # ======================================

    def connect(self):

        print("Conectando al broker MQTT...")

        self.client.connect(

            self.BROKER,

            self.PORT
        )

        self.client.loop_start()

    # ======================================
    # CUANDO CONECTA
    # ======================================

    def on_connect(self, client, userdata, flags, rc):

        if rc == 0:

            print("Conectado correctamente")

            self.client.subscribe(
                "sistema/sensor/temperatura"
            )

            self.client.subscribe(
                "sistema/sensor/humedad_aire"
            )

            self.client.subscribe(
                "sistema/sensor/humedad_suelo1"
            )

            self.client.subscribe(
                "sistema/sensor/humedad_suelo2"
            )

            self.client.subscribe(
                "sistema/estado/#"
            )

            self.client.subscribe(
                "sistema/pong"
            )

        else:

            print("Error de conexión:", rc)

    # ======================================
    # RECIBIR MENSAJES
    # ======================================

    def on_message(self, client, userdata, msg):

        topic = msg.topic

        payload = msg.payload.decode()

        print("========================")
        print("TOPIC:", topic)
        print("MENSAJE:", payload)
        print("========================")

        # =========================
        # PONG ESP32
        # =========================

        if topic == "sistema/pong":

            self.esp32_online = True

            self.last_pong = time.time()

            print("ESP32 ONLINE")

        # =========================
        # TEMPERATURA
        # =========================

        elif topic == "sistema/sensor/temperatura":

            self.temperatura = payload

        # =========================
        # HUMEDAD AIRE
        # =========================

        elif topic == "sistema/sensor/humedad_aire":

            self.humedad_aire = payload

        # =========================
        # HUMEDAD SUELO 1
        # =========================

        elif topic == "sistema/sensor/humedad_suelo1":

            self.humedad_suelo1 = payload

        # =========================
        # HUMEDAD SUELO 2
        # =========================

        elif topic == "sistema/sensor/humedad_suelo2":

            self.humedad_suelo2 = payload

    # ======================================
    # PUBLICAR
    # ======================================

    def publish(self, topic, data):

        payload = json.dumps(data)

        self.client.publish(
            topic,
            payload
        )

    # ======================================
    # DESCONECTAR
    # ======================================

    def on_disconnect(self, client, userdata, rc):

        print("Desconectado del broker")

    # ======================================
    # ENVIAR PING
    # ======================================

    def enviar_ping(self):

        ping = {
            "ping": True
        }

        self.client.publish(

            "sistema/ping",

            json.dumps(ping)
        )

    # ======================================
    # VERIFICAR ESP32
    # ======================================

    def verificar_esp32(self):

        tiempo = time.time()

        if tiempo - self.last_pong > 10:

            self.esp32_online = False

            self.temperatura = "--"

            self.humedad_aire = "--"

            self.humedad_suelo1 = "--"

            self.humedad_suelo2 = "--"

            print("ESP32 OFFLINE")