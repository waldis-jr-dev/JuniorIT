'''ввести текст и число
если дл. текста равна числу и число /17 больше 3, то печатаем \good\
если меньше 3, то \not bad\
в остальных случаях  выводим \bad'''

text = input("enter text: ")
number = input("enter number: ")

if len(text) == len(number) :
    if int(number) / 3 > 17:
        print("good")
    if int(number) / 3 < 17:
        print("not bad")
else :
    print("bad")
