# screens/splash_screen.py

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.screen import MDScreen
# =========================
# KV DESIGN
# =========================

KV = '''

<SplashScreen>:
    name: "splash"

    MDFloatLayout:

        canvas.before:
            Color:
                rgba: 0.05, 0.08, 0.12, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDIcon:
            id: logo
            icon: "water"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0.8, 1, 1
            font_size: "100sp"
            pos_hint: {"center_x": .5, "center_y": .62}
            opacity: 0

        MDLabel:
            id: title
            text: "Hydronix"
            halign: "center"
            font_style: "H2"
            bold: True
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_y": .46}
            opacity: 0

        MDLabel:
            id: subtitle
            text: "Smart Irrigation System"
            halign: "center"
            theme_text_color: "Custom"
            text_color: .7, .7, .7, 1
            pos_hint: {"center_y": .40}
            opacity: 0

        MDSpinner:
            size_hint: None, None
            size: dp(50), dp(50)
            pos_hint: {"center_x": .5, "center_y": .25}
            active: True
'''

# CARGAR KV
Builder.load_string(KV)

# =========================
# CLASE SPLASH
# =========================

class SplashScreen(MDScreen):
    def on_enter(self):

        Clock.schedule_once(
            self.start_animations,
            0.2
        )

    def start_animations(self, *args):

        Animation(
            opacity=1,
            d=1.2
        ).start(self.ids.logo)

        Animation(
            opacity=1,
            d=1.6
        ).start(self.ids.title)

        Animation(
            opacity=1,
            d=2
        ).start(self.ids.subtitle)

        Clock.schedule_once(
            self.change_screen,
            3
        )

    def change_screen(self, *args):

        self.manager.current = "main"


# =========================
# FUNCIÓN PARA INVOCAR
# =========================

def get_splash_screen():

    return SplashScreen(name="splash")