"""
Dummy mobile client for testing GET and POST requests.
"""
import json
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

    def _post(self) -> None:
        # This was a struggle to implements.
        # Things I learned
        # - headers MUST be Dict
        # - body MUST by str
        # - <timeout> will not error, need to also provide <on_error> callback
        UrlRequest(
            'http://localhost:8000/post/',
            req_headers={'Content-Type': 'application/json'},
            req_body=json.dumps({'number': 1, 'text': 'first'}),
            on_success=self._update_label,
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
