def show_by_one(a):
    for i in a:
        yield i
answ = show_by_one('abcd')
print(next(answ))
print(next(answ))
