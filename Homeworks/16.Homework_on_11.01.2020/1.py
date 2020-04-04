'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
'''
from colorama import Fore, Back, Style
file = open('/home/waldis/Documents/Python/Homeworks/16.Homework_on_11.01.2020/word.txt')
word = list(file.read())
answ = []
for i in range(len(word)):
    answ.append('_')
out = ''
for i in answ:
    out += i + ' '
print(Fore.CYAN, out, Style.RESET_ALL, '\n')
incor = []
indt = 0
while indt <= 10:
    let = input(Fore.YELLOW + 'Enter letter: ' + Style.RESET_ALL)
    if let == 'quit':
        break
    if not let.isalpha() or len(let) > 1:
        print(Fore.WHITE, Back.RED, 'Incorrect input!', Style.RESET_ALL)
    else:
        file = False
        for i in range(len(word)):
            if let == word[i]:
                file = True
                answ[i] = word[i]
        if file == False:
            if let not in incor:
                print('\n', Fore.RED, 'Incorrect (', Style.RESET_ALL)
                incor.append(let)
                indt += 1
            else:
                print('You have already entered this letter, and it is incorrect ! ')
        else:
            print(Fore.GREEN, 'Correct !', Style.RESET_ALL)
        if answ == word:
            print(Back.RED, Fore.GREEN, 'You WON !', Style.RESET_ALL)
            break
        if indt == 1:
            print('    \n    \n    \n   _\n')
        if indt == 2:
            print('    \n    \n    \n ___\n')
        if indt == 3:
            print('    \n    \n    \n|___\n')
        if indt == 4:
            print('    \n    \n|   \n|___\n')
        if indt == 5:
            print('    \n|   \n|   \n|___\n')
        if indt == 6:
            print(' _  \n|   \n|   \n|___\n')
        if indt == 7:
            print(' _ _\n|   \n|   \n|___\n')
        if indt == 8:
            print(' _ _\n|  o\n|   \n|___\n')
        if indt == 9:
            print(' _ _\n|  o\n| / \n|___\n')
        if indt == 10:
            print(' _ _\n|  o\n| /|\n|___\n')
            print(Fore.BLUE, 'You lose (', Style.RESET_ALL)
            break
        out = ''
        for i in answ:
            out += i + ' '
        print('\n', Fore.CYAN, out, Style.RESET_ALL)
        out = ''
        for i in incor:
            out += i + ', '
        print(Fore.RED, 'Incorrect letters: ', out, Style.RESET_ALL)