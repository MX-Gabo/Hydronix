# screens/home/home_screen.py

from mqtt.global_mqtt import mqtt_global

from kivy.lang import Builder
from kivy.clock import Clock

from kivymd.uix.boxlayout import MDBoxLayout

KV = '''

<HomeScreen>

    orientation: "vertical"

    canvas.before:
        Color:
            rgba: 0.05, 0.07, 0.10, 1
        Rectangle:
            pos: self.pos
            size: self.size

    ScrollView:

        MDBoxLayout:
            orientation: "vertical"
            adaptive_height: True
            spacing: "18dp"
            padding: "15dp"

            # =====================================
            # HEADER
            # =====================================

            MDBoxLayout:
                adaptive_height: True
                spacing: "10dp"

                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True

                    MDLabel:
                        text: "Hydronix"
                        font_style: "H3"
                        bold: True

                    MDLabel:
                        text: "Sistema Inteligente de Riego"
                        theme_text_color: "Secondary"

                MDIconButton:
                    icon: "account-circle"
                    user_font_size: "35sp"

            # =====================================
            # ESTADO ESP32
            # =====================================

            MDCard:
                id: card_estado
                radius: [25]
                padding: "20dp"
                size_hint_y: None
                height: "100dp"
                md_bg_color: 0.25, 0.08, 0.08, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        id: icon_estado
                        icon: "wifi-off"
                        theme_text_color: "Custom"
                        text_color: 1, 0.3, 0.3, 1
                        font_size: "40sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            id: estado_esp32
                            text: "ESP32 Offline"
                            bold: True

                        MDLabel:
                            text: "Broker MQTT"
                            theme_text_color: "Secondary"

            # =====================================
            # TEMPERATURA
            # =====================================

            MDCard:
                radius: [30]
                padding: "25dp"
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.15, 0.12, 0.12, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDIcon:
                        icon: "thermometer"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 0.4, 0.4, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Temperatura"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: temperatura
                        text: "0 °C"
                        halign: "center"
                        font_style: "H2"

            # =====================================
            # HUMEDAD AIRE
            # =====================================

            MDCard:
                radius: [30]
                padding: "25dp"
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.10, 0.15, 0.22, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDIcon:
                        icon: "water-percent"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0, 0.8, 1, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Humedad Aire"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: humedad_aire
                        text: "0 %"
                        halign: "center"
                        font_style: "H2"

            # =====================================
            # HUMEDAD SUELO 1
            # =====================================

            MDCard:
                radius: [30]
                padding: "25dp"
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.10, 0.18, 0.12, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDIcon:
                        icon: "sprout"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.2, 1, 0.4, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Humedad Suelo 1"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: humedad_suelo1
                        text: "0 %"
                        halign: "center"
                        font_style: "H2"

            # =====================================
            # HUMEDAD SUELO 2
            # =====================================

            MDCard:
                radius: [30]
                padding: "25dp"
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.10, 0.16, 0.10, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDIcon:
                        icon: "leaf"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.4, 1, 0.5, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Humedad Suelo 2"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: humedad_suelo2
                        text: "0 %"
                        halign: "center"
                        font_style: "H2"

            # =====================================
            # PROMEDIO HUMEDAD
            # =====================================

            MDCard:
                radius: [30]
                padding: "25dp"
                size_hint_y: None
                height: "180dp"
                md_bg_color: 0.12, 0.12, 0.22, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "10dp"

                    MDIcon:
                        icon: "chart-line"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 0.8, 0.2, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Promedio Humedad"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDLabel:
                        id: promedio
                        text: "0 %"
                        halign: "center"
                        font_style: "H2"
'''

Builder.load_string(KV)

class HomeScreen(MDBoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


        self.mqtt = mqtt_global

        Clock.schedule_interval(
            self.actualizar_ui,
            1
        )

        Clock.schedule_interval(
            self.enviar_ping,
            5
        )

    # ==================================
    # ACTUALIZAR UI
    # ==================================

    def actualizar_ui(self, dt):

        self.mqtt.verificar_esp32()

        # ==========================
        # ESTADO ESP32
        # ==========================

        if self.mqtt.esp32_online:

            self.ids.estado_esp32.text = "ESP32 Conectado"

            self.ids.card_estado.md_bg_color = (
                0.08, 0.25, 0.12, 1
            )

            self.ids.icon_estado.icon = "wifi"

            self.ids.icon_estado.text_color = (
                0.2, 1, 0.4, 1
            )

        else:

            self.ids.estado_esp32.text = "ESP32 Offline"

            self.ids.card_estado.md_bg_color = (
                0.25, 0.08, 0.08, 1
            )

            self.ids.icon_estado.icon = "wifi-off"

            self.ids.icon_estado.text_color = (
                1, 0.3, 0.3, 1
            )

        # ==========================
        # SENSORES
        # ==========================

        self.ids.temperatura.text = (
            f"{self.mqtt.temperatura} °C"
        )

        self.ids.humedad_aire.text = (
            f"{self.mqtt.humedad_aire} %"
        )

        self.ids.humedad_suelo1.text = (
            f"{self.mqtt.humedad_suelo1} %"
        )

        self.ids.humedad_suelo2.text = (
            f"{self.mqtt.humedad_suelo2} %"
        )

        # ==========================
        # PROMEDIO
        # ==========================

        try:

            promedio = (

                int(self.mqtt.humedad_suelo1)

                +

                int(self.mqtt.humedad_suelo2)

            ) / 2

            self.ids.promedio.text = (
                f"{int(promedio)} %"
            )

        except:

            self.ids.promedio.text = "0 %"

    # ==================================
    # ENVIAR PING
    # ==================================

    def enviar_ping(self, dt):

        self.mqtt.enviar_ping()