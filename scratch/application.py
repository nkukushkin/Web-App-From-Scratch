from .request import Request
from .response import Response

class Application:
    def __call__(self, request: Request) -> Response:
        return Response("501 Not Implemented", content="Not Implemented")