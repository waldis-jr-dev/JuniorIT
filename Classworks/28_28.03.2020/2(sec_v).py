def dictionary(name):
    with open(name, 'r', encoding='utf-8') as file:
        data = file.read()
    data = data.split(', ')
    dict1 = {}
    for i in data:
        i = i.split()
        dict1[i[0]] = i[1]
    return dict1


def synomims(dictionary, value):
    if value in dictionary:
        return dictionary[value]
    elif value in dictionary.values():
        for i in dictionary.keys():
            if dictionary[i] == value:
                return i
    else:
        return 'We cannot find it'


a = dictionary('1.txt')
print(synomims(a, 'eg'))