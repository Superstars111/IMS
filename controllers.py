from windows import IMSWindow
from functools import partial


class IMS:
    """Main IMS Controller Class"""

    def __init__(self, model, view):
        self._model = model
        self._view = view
