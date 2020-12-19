import json
import requests
from typing import Union, List, Type, Optional
from abstract_crawler import AbstractEngine, AbstractCrawler, AbstractParser


class Engine(AbstractEngine):
    @classmethod
    def get(cls, link) -> requests.Response:
        resp = requests.get(link)
        return resp

    @classmethod
    def post(cls, link: str, data: dict = None) -> requests.Response:
        if data is None:
            resp = requests.post(link)
        else:
            resp = requests.post(link, json=data)
        return resp


class NumbersAPICrawler(AbstractCrawler):
    def __init__(self, numbers: List[Union[int]]):
        self._numbers = numbers
        self._engine = self._set_engine()
        self._parser = self._set_parser()

    @classmethod
    def _set_engine(cls) -> Type[AbstractEngine]:
        return Engine

    @classmethod
    def _set_parser(cls) -> Type[AbstractParser]:
        return NumbersAPIParser

    @classmethod
    def domain(cls) -> str:
        return 'numbersapi.com'

    @classmethod
    def create_search_url(cls, numbers: List[int]) -> str:
        numbers_str = ','.join([str(x) for x in numbers])
        return f'http://{cls.domain()}/{numbers_str}'

    def get_number_by_index(self, index: int) -> Optional[int]:
        try:
            return self._numbers[index]
        except IndexError:
            return None

    def change_number_by_index(self, new_number: int, index: int) -> None:
        if len(self._numbers) > index:
            self._numbers[index] = new_number
            return
        raise IndexError('Index is out of range. We can not set new value')

    def crawl(self):
        url = self.create_search_url(self._numbers)
        response = self._engine.get(url)
        return self._parser.parse(response)


class NumbersAPIParser(AbstractParser):
    @classmethod
    def parse(cls, response: requests.Response) -> Union[dict, str]:
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            return response.text


if __name__ == '__main__':
    crawler = NumbersAPICrawler([42, 789, 4])
    print(crawler.crawl())
