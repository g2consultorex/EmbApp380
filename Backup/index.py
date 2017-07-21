from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition


class IndexScreen(Screen):
    def disconnect(self):
        print "Awebo"
