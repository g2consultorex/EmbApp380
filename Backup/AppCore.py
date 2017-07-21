from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '1080')
Config.set('graphics', 'height', '720')


from kivy.app import App
# from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.screenmanager import Screen

# from gestordb import ModeloLog

from index import IndexScreen
from createlabel import CreateLabelScreen


class LoginScreen(Screen):

    field_user = ObjectProperty()
    field_password = ObjectProperty()

    def validate_DB(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "create_label"
        print "validando"


class LoginApp(App):

    title = "EmbApp380"

    def build(self):

        screen_manager = ScreenManager()
        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(IndexScreen(name="index"))
        screen_manager.add_widget(CreateLabelScreen(name="create_label"))

        return screen_manager


if __name__ == "__main__":
    LoginApp().run()
