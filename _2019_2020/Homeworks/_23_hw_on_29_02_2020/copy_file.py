def copy_file(what, to):
    with open(what, 'rb') as f1, open(to, 'wb') as f2:
        for i in f1:
            f2.write(i)
    return None

