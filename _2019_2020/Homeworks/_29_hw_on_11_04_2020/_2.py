while True:
    a = input('>>> ')
    if not a.isdigit():
        raise TypeError('Not digit ')