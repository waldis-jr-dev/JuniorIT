is_none = lambda x: x if x is not None else -1
is_str = lambda x: x if isinstance(x, str) else str(x)
list = [1, 4, 'rtt', None]
list_new = []
for i in list:
    list_new.append(is_str(is_none(i)))
print(list_new)