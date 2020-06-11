import string
ab = ['abc','cv','Fd','fg','eYty','eryT',]


def f(a):
    abc = string.ascii_lowercase
    minn = len(ab[0])
    for i in a:
        if len(i) <= minn:
            minn = len(i)
    varients = []
    for i in a:
        if len(i) == minn:
            i = i.lower()
            varients.append(i)


c = f(ab)
print(c)

