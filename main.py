from kivy.utils import platform
from kivy.core.window import Window
from kivy.metrics import dp, sp

# Solo fijar tamaño en PC/desarrollo
if platform != 'android':
    Window.size = (390, 844)

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.splash_screen import get_splash_screen
from screens.main_screen import MainScreen


class HydronixApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        # Calcular factor de escala según ancho real de pantalla
        # Base de diseño: 390px (Reno 13 / iPhone 14)
        base_width = 390.0
        self._scale = Window.width / base_width

        sm = MDScreenManager()
        sm.add_widget(get_splash_screen())
        sm.add_widget(MainScreen(name="main"))
        return sm

    def s(self, value):
        """
        Escala cualquier valor dp/sp automáticamente.
        Uso en KV:  height: app.s("180dp")
                    font_size: app.s("35sp")
                    spacing: app.s("12dp")
        """
        value = str(value).strip()

        if value.endswith("dp"):
            return dp(float(value[:-2])) * self._scale
        elif value.endswith("sp"):
            return sp(float(value[:-2])) * self._scale
        else:
            return float(value) * self._scale


HydronixApp().run()