from collections import namedtuple


def change(old_namedtuple, new_args: dict):

    New = namedtuple(old_namedtuple.__name__, list(set(list(new_args.keys())+list(old_namedtuple._fields))))
    return New(*new_args.values())


Person = namedtuple('Person', ['name', 'surname'])
test1 = Person('Cris', 'Evan')
args = {'name': 'None', 'color': 'red'}

print(change(test1, args))
