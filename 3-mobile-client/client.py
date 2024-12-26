"""
Dummy mobile client for testing GET and POST requests.
"""
from typing import Any
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class HttpButtons(BoxLayout):
    """A button each for GET and POST requests, and a label for results. """
    _label = ObjectProperty(None)

    def _get(self) -> None:
        UrlRequest(
            'http://localhost:8000/get/',
            on_success=self._update_label
        )

    def _update_label(
        self,
        req: UrlRequest,
        result: Any
    ) -> None:
        """Update app label.

        Args:
            req (UrlRequest): HTTP(S) request
            result (Any): request result
        """
        self._label.text = result['message']


class ClientApp(App):
    """Main application class. """
    def build(self) -> None:
        return HttpButtons()


if __name__ == '__main__':
    ClientApp().run()
