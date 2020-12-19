def terraflew(amount):
    def add_terraflew(function):
        def wrapper(self, taste):
            data = function(self, taste) + ' Added conoterraflew' * amount
            return data
        return wrapper
    return add_terraflew


class Cookies:
    @terraflew(amount=3)
    def make_cookie(self, taste):
        return f'Tasty {taste} COOKIE'


print(Cookies().make_cookie('COCONUT'))