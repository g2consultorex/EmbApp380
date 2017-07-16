
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen


class ScreenPresentation(Screen):

    def goto_Index(self):
        print "Hola"


class ScreenIndex(Screen):
    pass


class AdminPantallas(ScreenManager):
    pass


presentacion = Builder.load_file("AppGUI.kv")

# screen_manager.add_widget(ScreenPresentation(name="presentacion"))
# screen_manager.add_widget(ScreenIndex(name="index"))


class AppGUI(App):

    def build(self):
        return presentacion


if __name__ == "__main__":
    AppGUI().run()
