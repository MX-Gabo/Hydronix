# screens/configuracion/configuracion_screen.py

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''

<ConfiguracionScreen>

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
                        text: "Configuración"
                        font_style: "H2"
                        bold: True

                    MDLabel:
                        text: "Configuración del sistema y MQTT"
                        theme_text_color: "Secondary"

                MDIconButton:
                    icon: "cog"
                    user_font_size: "35sp"

            # =====================================
            # MANTENIMIENTO
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "190dp"
                md_bg_color: 0.22, 0.16, 0.08, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "tools"
                        theme_text_color: "Custom"
                        text_color: 1, 0.7, 0.2, 1
                        font_size: "60sp"

                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "10dp"

                        MDLabel:
                            text: "Sección en Mantenimiento"
                            font_style: "H5"
                            bold: True

                        MDLabel:
                            text: "La configuración avanzada del broker MQTT aún está en desarrollo."

                    
            # =====================================
            # INFORMACION APP
            # =====================================

            MDCard:
                radius: [25]
                padding: "20dp"
                size_hint_y: None
                height: "150dp"
                md_bg_color: 0.10, 0.18, 0.12, 1

                MDBoxLayout:
                    orientation: "vertical"

                    MDLabel:
                        text: "Hydronix"
                        font_style: "H5"

                    MDLabel:
                        text: "Sistema Inteligente de Riego"

                    MDLabel:
                        text: "Versión: 1.0 Beta"

                    MDLabel:
                        text: "ESP32 + MQTT + Python"
                        theme_text_color: "Secondary"
'''

Builder.load_string(KV)


class ConfiguracionScreen(MDBoxLayout):
    pass