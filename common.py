from typing import Union


def pathjoin(*args: Union[int, str]) -> str:
    return "/".join(str(arg).lstrip("/") for arg in args)