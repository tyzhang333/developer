import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser


PORT = int(os.environ.get("PORT", "8000"))
HOST = os.environ.get("HOST", "127.0.0.1")


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    server = ThreadingHTTPServer((HOST, PORT), QuietHandler)
    url = f"http://{HOST}:{PORT}"
    print(f"Serving {root}")
    print(f"Open {url}")
    if not os.environ.get("COLAB_RELEASE_TAG"):
        try:
            webbrowser.open(url)
        except Exception:
            pass
    server.serve_forever()
