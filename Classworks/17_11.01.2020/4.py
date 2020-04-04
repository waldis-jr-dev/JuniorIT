def age():
    age = int(input('Enter your age: '))
    if 0 < age < 127:
        answ = age - 2
        if answ < 0:
            print('You 1 ear old')
        else:
            print(answ)
    else:
        print('You lie')


age()