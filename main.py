from kivy.core.window import Window

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.splash_screen import get_splash_screen
from screens.main_screen import MainScreen

# Tamaño ventana
Window.size = (360, 640)


class HydronixApp(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        # SCREEN MANAGER
        sm = MDScreenManager()

        # SPLASH
        sm.add_widget(
            get_splash_screen()
        )

        # MAIN SCREEN
        sm.add_widget(
            MainScreen(name="main")
        )

        return sm


HydronixApp().run()