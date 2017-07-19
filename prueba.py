from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class AddLocationForm(BoxLayout):

    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        casa = self.search_input.text
        data = [
            casa,
            'casa',
            'perro',
            'animal',
        ]
        self.found_location(data)

    def found_location(self, data):
        self.search_results.item_strings = data


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
