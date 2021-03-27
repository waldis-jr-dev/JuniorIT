a = 7
def func():
    global a
    a += 1
    return True
func()
print(a)