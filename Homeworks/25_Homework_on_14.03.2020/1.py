import random, time


def monkey(word):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    new_word = ''
    start = time.time()
    for i in word:
        new_word += random.choice(abc)
    while True:
        if new_word == word:
            end = time.time()
            break
        else:
            new_word = new_word[1:len(new_word):]
            new_word += random.choice(abc)
    return end - start

word = input('Enter word: ')
print(monkey(word))