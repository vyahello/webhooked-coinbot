from abc import ABC, abstractmethod
from re import search


class Text(ABC):
    """Abstraction of a text."""

    @abstractmethod
    def match(self) -> bool:
        pass

    @abstractmethod
    def get_coin(self) -> str:
        pass


class InputText(Text):
    """Parse input message."""

    def __init__(self, text: str, pattern: str = r"/\w+") -> None:
        self._pattern: str = pattern
        self._text: str = text

    def match(self) -> bool:
        return search(self._pattern, self._text)

    def get_coin(self) -> str:
        return self.match().group()
