import sys

from .application import Application
from .server import HTTPServer

def main() -> int:
    application = Application()

    server = HTTPServer()
    server.mount("", application)
    server.serve_forever()
    return 0

if __name__ == "__main__":
    sys.exit(main())
