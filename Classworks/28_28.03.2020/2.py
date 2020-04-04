def calc_word(word = ''):
    with open('dict_s.txt', 'r') as file:
        data = file.read()
    data = data.split(', ')
    news = {}
    for i in data:
        i = i.split(' ')
        news[i[0]] = i[1]
    for i in news.items():
        for u in range(len(i)):
            if i[u] == word:
                if u == 0:
                    return i[1]
                if u == 1:
                    return i[0]


while True:
    word = input('Enter word: ')
    print(calc_word(word))