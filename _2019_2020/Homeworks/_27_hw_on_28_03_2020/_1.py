def calc(name):
    with open(name, 'r') as file:
        data = file.read()
    result = {}
    for i in data:
        if i in result.keys():
            result[i] += 1
        else:
            result[i] = 1
    return result



print(calc('file.txt'))
