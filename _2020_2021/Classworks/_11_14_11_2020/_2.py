import requests


class NumbersFacts:
    def __getattr__(self, item):
        print('New attribute')
        if item[0:2] == '_n' and item[2:].isdigit():
            resp = requests.get(f'http://numbersapi.com/{item[2::]}').text
            self.__dict__[item] = resp
            return resp


fact = NumbersFacts()
print(fact._n122)
print(fact._n122)
