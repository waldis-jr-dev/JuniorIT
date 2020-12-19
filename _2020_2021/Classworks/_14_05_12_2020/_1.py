def terraflew(amount):
    def add_terraflew(function):
        def wrapper(taste):
            data = function(taste) + ' Added conoterraflew' * amount
            return data
        return wrapper
    return add_terraflew


@terraflew(amount=3)
def make_cookie(taste):
    return f'Tasty {taste} COOKIE'
