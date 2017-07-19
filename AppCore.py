
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

# from gestordb import ModeloLog


presentacion = Builder.load_file("AppGUI.kv")


class ScreenPresentation(Screen):

    def validate_DB(self):
        pass
        # ModeloLog.add('Inicio de la APP', "El usuario inicio en la app")


class ScreenIndex(Screen):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(ScreenPresentation(name="presentacion"))
screen_manager.add_widget(ScreenIndex(name="index"))


class AppGUI(App):

    def build(self):
        # self.title = "EmbApp380"
        return screen_manager


if __name__ == "__main__":
    AppGUI().run()
