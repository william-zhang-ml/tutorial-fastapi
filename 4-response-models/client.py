"""
Dummy mobile client for testing GET and POST requests.
"""
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class HttpButtons(BoxLayout):
    """A button each for GET and POST requests, and a label for results. """
    _label = ObjectProperty(None)

    def _get(self) -> None:
        req = UrlRequest('http://localhost:8000/get/')
        req.wait(0)
        print(f'Response type: {type(req.result)}')
        for key, value in req.result.items():
            print(f'Key ({type(key)}): {key}')
            print(f'Value ({type(value)}): {value}')


class ClientApp(App):
    """Main application class. """
    def build(self) -> None:
        return HttpButtons()


if __name__ == '__main__':
    ClientApp().run()
