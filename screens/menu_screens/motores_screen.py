# screens/motores/motores_screen.py

from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout

from mqtt.global_mqtt import mqtt_global

KV = '''

<MotoresScreen>

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
                        text: "Motores"
                        font_style: "H3"
                        bold: True

                    MDLabel:
                        text: "Control Inteligente de Bombas"
                        theme_text_color: "Secondary"

                MDIconButton:
                    icon: "engine"
                    user_font_size: "35sp"

            # =====================================
            # ESTADO GENERAL
            # =====================================

            MDCard:
                radius: [25]
                padding: "20dp"
                size_hint_y: None
                height: "120dp"
                md_bg_color: 0.10, 0.18, 0.12, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "water-pump"
                        theme_text_color: "Custom"
                        text_color: 0.2, 1, 0.4, 1
                        font_size: "45sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            text: "Sistema de Bombas"
                            bold: True

                        MDLabel:
                            text: "2 bombas conectadas"
                            theme_text_color: "Secondary"

                        MDLabel:
                            id: estado_general
                            text: "Todas apagadas"
                            theme_text_color: "Secondary"

            # =====================================
            # BOTONES GENERALES
            # =====================================

            MDGridLayout:
                cols: 2
                spacing: "10dp"
                size_hint_y: None
                height: "55dp"

                MDRaisedButton:
                    text: "ENCENDER TODAS"
                    md_bg_color: 0.1, 0.7, 0.3, 1
                    on_release:
                        root.encender_todas()

                MDRaisedButton:
                    text: "APAGAR TODAS"
                    md_bg_color: 0.8, 0.2, 0.2, 1
                    on_release:
                        root.apagar_todas()

            # =====================================
            # BOMBA 1
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "300dp"
                md_bg_color: 0.12, 0.15, 0.22, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "15dp"

                    MDIcon:
                        icon: "water-pump"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0, 0.8, 1, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Bomba 1"
                        halign: "center"
                        font_style: "H5"

                    MDLabel:
                        id: estado_bomba1
                        text: "Estado: APAGADA"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDGridLayout:
                        cols: 2
                        spacing: "10dp"
                        size_hint_y: None
                        height: "50dp"

                        MDRaisedButton:
                            text: "ENCENDER"
                            md_bg_color: 0.1, 0.7, 0.3, 1
                            on_release:
                                root.encender_bomba1()

                        MDRaisedButton:
                            text: "APAGAR"
                            md_bg_color: 0.8, 0.2, 0.2, 1
                            on_release:
                                root.apagar_bomba1()

                    MDLabel:
                        text: "Control individual MQTT"
                        halign: "center"
                        theme_text_color: "Secondary"

            # =====================================
            # BOMBA 2
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "300dp"
                md_bg_color: 0.12, 0.15, 0.22, 1

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "15dp"

                    MDIcon:
                        icon: "water-pump"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.2, 1, 0.4, 1
                        font_size: "55sp"

                    MDLabel:
                        text: "Bomba 2"
                        halign: "center"
                        font_style: "H5"

                    MDLabel:
                        id: estado_bomba2
                        text: "Estado: APAGADA"
                        halign: "center"
                        theme_text_color: "Secondary"

                    MDGridLayout:
                        cols: 2
                        spacing: "10dp"
                        size_hint_y: None
                        height: "50dp"

                        MDRaisedButton:
                            text: "ENCENDER"
                            md_bg_color: 0.1, 0.7, 0.3, 1
                            on_release:
                                root.encender_bomba2()

                        MDRaisedButton:
                            text: "APAGAR"
                            md_bg_color: 0.8, 0.2, 0.2, 1
                            on_release:
                                root.apagar_bomba2()

                    MDLabel:
                        text: "Control individual MQTT"
                        halign: "center"
                        theme_text_color: "Secondary"
'''

Builder.load_string(KV)


class MotoresScreen(MDBoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.mqtt = mqtt_global


    # =====================================
    # BOMBA 1
    # =====================================

    def encender_bomba1(self):

        self.mqtt.publish(

            "sistema/bombas/bomba1",

            {
                "estado": "on"
            }
        )

        self.ids.estado_bomba1.text = (
            "Estado: ENCENDIDA"
        )

        print("Bomba 1 ON")

    def apagar_bomba1(self):

        self.mqtt.publish(

            "sistema/bombas/bomba1",

            {
                "estado": "off"
            }
        )

        self.ids.estado_bomba1.text = (
            "Estado: APAGADA"
        )

        print("Bomba 1 OFF")

    # =====================================
    # BOMBA 2
    # =====================================

    def encender_bomba2(self):

        self.mqtt.publish(

            "sistema/bombas/bomba2",

            {
                "estado": "on"
            }
        )

        self.ids.estado_bomba2.text = (
            "Estado: ENCENDIDA"
        )

        print("Bomba 2 ON")

    def apagar_bomba2(self):

        self.mqtt.publish(

            "sistema/bombas/bomba2",

            {
                "estado": "off"
            }
        )

        self.ids.estado_bomba2.text = (
            "Estado: APAGADA"
        )

        print("Bomba 2 OFF")

    # =====================================
    # TODAS LAS BOMBAS
    # =====================================

    def encender_todas(self):

        self.mqtt.publish(

            "sistema/bombas/todas",

            {
                "estado": "on"
            }
        )

        self.ids.estado_general.text = (
            "Todas ENCENDIDAS"
        )

        self.ids.estado_bomba1.text = (
            "Estado: ENCENDIDA"
        )

        self.ids.estado_bomba2.text = (
            "Estado: ENCENDIDA"
        )

        print("Todas las bombas ON")

    def apagar_todas(self):

        self.mqtt.publish(

            "sistema/bombas/todas",

            {
                "estado": "off"
            }
        )

        self.ids.estado_general.text = (
            "Todas APAGADAS"
        )

        self.ids.estado_bomba1.text = (
            "Estado: APAGADA"
        )

        self.ids.estado_bomba2.text = (
            "Estado: APAGADA"
        )

        print("Todas las bombas OFF")