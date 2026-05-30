import threading
from typing import Callable


class FlaskThreadRunner:

    def __init__(self, app_instance, host: str, port: int):
        self._app = app_instance
        self._host = host
        self._port = port

    def _run(self) -> None:
        self._app.run(host=self._host, port=self._port, debug=False, use_reloader=False)

    def start_as_daemon(self) -> threading.Thread:
        server_thread = threading.Thread(target=self._run, daemon=True)
        server_thread.start()
        return server_thread
