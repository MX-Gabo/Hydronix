# screens/notificaciones/notificaciones_screen.py

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''

<NotificacionesScreen>

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
                        text: "Notificaciones"
                        font_style: "H3"
                        bold: True

                    MDLabel:
                        text: "Alertas y eventos del sistema"
                        theme_text_color: "Secondary"

                MDIconButton:
                    icon: "bell"
                    user_font_size: "35sp"

            # =====================================
            # ALERTA CRITICA
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "160dp"
                md_bg_color: 0.25, 0.10, 0.10, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "alert-circle"
                        theme_text_color: "Custom"
                        text_color: 1, 0.3, 0.3, 1
                        font_size: "50sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            text: "Humedad Baja"
                            font_style: "H5"
                            bold: True

                        MDLabel:
                            text: "La humedad del suelo está por debajo del nivel recomendado."

                        MDLabel:
                            text: "Hace 2 minutos"
                            theme_text_color: "Secondary"

            # =====================================
            # SISTEMA ONLINE
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "160dp"
                md_bg_color: 0.10, 0.18, 0.12, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "check-circle"
                        theme_text_color: "Custom"
                        text_color: 0.2, 1, 0.4, 1
                        font_size: "50sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            text: "Sistema Online"
                            font_style: "H5"
                            bold: True

                        MDLabel:
                            text: "Todos los sensores y bombas funcionan correctamente."

                        MDLabel:
                            text: "Hace 5 minutos"
                            theme_text_color: "Secondary"

            # =====================================
            # BOMBA ACTIVADA
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "160dp"
                md_bg_color: 0.10, 0.15, 0.22, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "water-pump"
                        theme_text_color: "Custom"
                        text_color: 0, 0.8, 1, 1
                        font_size: "50sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            text: "Bomba Activada"
                            font_style: "H5"
                            bold: True

                        MDLabel:
                            text: "La bomba 2 fue encendida automáticamente."

                        MDLabel:
                            text: "Hace 10 minutos"
                            theme_text_color: "Secondary"

            # =====================================
            # SENSOR DESCONECTADO
            # =====================================

            MDCard:
                radius: [30]
                padding: "20dp"
                size_hint_y: None
                height: "160dp"
                md_bg_color: 0.22, 0.16, 0.08, 1

                MDBoxLayout:
                    spacing: "15dp"

                    MDIcon:
                        icon: "wifi-off"
                        theme_text_color: "Custom"
                        text_color: 1, 0.7, 0.2, 1
                        font_size: "50sp"

                    MDBoxLayout:
                        orientation: "vertical"

                        MDLabel:
                            text: "Sensor Desconectado"
                            font_style: "H5"
                            bold: True

                        MDLabel:
                            text: "El sensor de humedad del suelo perdió conexión."

                        MDLabel:
                            text: "Hace 30 minutos"
                            theme_text_color: "Secondary"

            # =====================================
            # LIMPIAR ALERTAS
            # =====================================

            MDRaisedButton:
                text: "LIMPIAR NOTIFICACIONES"
                icon: "delete"
                size_hint_y: None
                height: "55dp"
'''

Builder.load_string(KV)


class NotificacionesScreen(MDBoxLayout):
    pass