# screens/main_screen.py

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# IMPORTAR PANTALLAS
from screens.menu_screens.home_screen import HomeScreen
from screens.menu_screens.motores_screen import MotoresScreen
from screens.menu_screens.notificaciones_screen import NotificacionesScreen
from screens.menu_screens.configuracion_screen import ConfiguracionScreen

KV = '''

<MainScreen>

    name: "main"

    MDBottomNavigation:

        panel_color: 0.05, 0.08, 0.12, 1
        text_color_active: 0, 0.8, 1, 1

        # =====================================
        # HOME
        # =====================================

        MDBottomNavigationItem:
            name: "home"
            text: "Inicio"
            icon: "home"

            HomeScreen:

        # =====================================
        # MOTORES
        # =====================================

        MDBottomNavigationItem:
            name: "motores"
            text: "Motores"
            icon: "engine"

            MotoresScreen:

        # =====================================
        # NOTIFICACIONES
        # =====================================

        MDBottomNavigationItem:
            name: "notificaciones"
            text: "Alertas"
            icon: "bell"

            NotificacionesScreen:

        # =====================================
        # CONFIGURACION
        # =====================================

        MDBottomNavigationItem:
            name: "config"
            text: "Config"
            icon: "cog"

            ConfiguracionScreen:
'''

Builder.load_string(KV)


class MainScreen(MDScreen):
    pass