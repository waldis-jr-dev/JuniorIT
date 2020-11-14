from typing import Union, Type
from abc import ABC, abstractmethod
import requests


class AbstractEngine(ABC):
    @classmethod
    @abstractmethod
    def get(cls, link) -> requests.Response:
        pass


class AbstractParser(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, response: requests.Response) -> Union[dict, str]:
        pass


class AbstractCrawler(ABC):
    @classmethod
    @abstractmethod
    def _set_engine(cls) -> Type[AbstractEngine]:
        pass

    @classmethod
    @abstractmethod
    def _set_parser(cls) -> Type[AbstractParser]:
        pass

    @abstractmethod
    def crawl(self):
        pass
