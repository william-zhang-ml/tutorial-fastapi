"""
Dummy mobile client for testing GET and POST requests.
"""
import json
from typing import Any
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CameraEcho(BoxLayout):
    """Interface for testing image sending and receiving. """
    _camera = ObjectProperty(None)
    _echo = ObjectProperty(None)

    def _post(self) -> None:
        # Get image from camera.
        data: bytes = self._camera.texture.pixels

        # Curate HTTP request body as-per API documentation.
        req_body = {
            'mode': self._camera.texture.colorfmt.upper(),
            'size': self._camera.texture.size,  # width, height
            'data': data.hex()
        }

        # Send request.
        UrlRequest(
            'http://127.0.0.1:8000/echo/',
            req_headers={'Content-Type': 'application/json'},
            req_body=json.dumps(req_body),
            on_success=self._update_echo,
        )

    def _update_echo(
        self,
        req: UrlRequest,
        result: Any
    ) -> None:
        """Update echo image from server.

        Args:
            req (UrlRequest): HTTP(S) request
            result (Any): request result
        """
        print(type(result))


class ClientApp(App):
    """Main application class. """
    def build(self) -> None:
        return CameraEcho()


if __name__ == '__main__':
    ClientApp().run()
