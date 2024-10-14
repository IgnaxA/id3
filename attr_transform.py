from typing import Callable, Any

class AttrTransform:
    def __init__(self, name, func: Callable[..., Any]):
        self.name = name
        self.func = func
