# app/lib/singletons.py

from typing import Any


class Singleton(type):
    _instances: dict[Any, Any] = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        # NOTE: commented else block to enable true singleton and no re-init of the class
        # else:
        #     cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]
