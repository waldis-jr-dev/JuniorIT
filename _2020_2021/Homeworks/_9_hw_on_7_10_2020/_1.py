import requests
from typing import Union, List, Type, Optional


class MetaEngine:
    pass


class MetaNumbersAPICrawler:
    pass


class MetaNumbersAPIParser:
    pass


class Engine(MetaEngine):
    @classmethod
    def get(cls, link: str) -> requests.Response:
        resp = requests.get(link)
        return resp

    @classmethod
    def post(cls, link: str, data: dict = None) -> requests.Response:
        if data is None:
            resp = requests.post(link)
        else:
            resp = requests.post(link, json=data)
        return resp


class NumbersAPICrawler(MetaNumbersAPICrawler):
    def __init__(self, numbers: List[Union[float, int]]):
        self._numbers = numbers
        self._engine = self.__set_engine()

    @staticmethod
    def __set_engine() -> Type[MetaEngine]:
        return Engine

    @classmethod
    def domain(cls) -> str:
        return 'numbersapi.com'

    @classmethod
    def create_search_url(cls, numbers: List[int]) -> str:
        numbers_str = ','.join([str(x) for x in numbers])
        return f"https://{cls.domain()}/{numbers_str}"

    def get_number_by_index(self, index: int) -> Optional[int]:
        try:
            return self._numbers[index]
        except IndexError:
            return

    def change_number_by_index(self, new_number: int, index: int) -> None:
        if len(self._numbers) > index:
            self._numbers[index] = new_number
            return
        raise IndexError('Index is out of range. We can not set new value')

    def crawl(self):
        url = self.create_search_url(self._numbers)
        response = self._engine.get(url)


class NumbersAPIParser(MetaNumbersAPIParser):
    def init(self, resp: requests.Response, *args, **kwargs):
        self.response = resp

    def get_useful_data(self, *args, **kwargs):
        return {
            "number": int(self.response.url.split("/")[-1]),
            "text": self.response.text,
        }

    def print_useful_data(self, *args, **kwargs):
        data = {
            "number": int(self.response.url.split("/")[-1]),
            "text": self.response.text,
        }
        if "is a boring number." in data["text"] or "is an unremarkable number." in data["text"] or\
                "is a number for which we're missing a fact (submit one to numbersapi at google mail!)." in data["text"] or\
                "is an uninteresting number." in data["text"]:
            print("We don't find any interesting facts about number", data["number"])
        else:
            print("Interesting fact about number", data["number"], ":", data["text"])
