pole = [['1 ', '2 ', '3 ', '4 ', '5 '],
        ['6 ', '7 ', '8 ', '9 ', '10'],
        ['11', '12', '13', '14', '15'],
        ['16', '17', '18', '19', '20'],
        ['21', '22', '23', '24', '25']]
players = ['X ', 'O ']
ch = 0
for i in pole:
    string = ''
    for j in i:
        string += j + '|'
    print(string[:-1])
print('Введите номер клеточки куда хотите походить.')
while True:
    if ch % 2 == 0:
        hod = input('Ход X: ')
        if not str(hod).isdigit() or int(hod) < 1 or int(hod) > 25:
            print('Некоректный ввод !')
            ch -= 1
        else:
            hod = int(hod) - 1
            xy = str(pole[hod // 5][hod % 5])[:1]
            if xy.isdigit():
                pole[hod // 5][hod % 5] = players[ch % 2]
            else:
                print('Там занято!')
                ch -= 1
    else:
        hod = input('Ход O: ')
        if not str(hod).isdigit() or int(hod) < 1 or int(hod) > 25:
            print('Некоректный ввод !')
            ch -= 1
        else:
            hod = int(hod) - 1
            xy = str(pole[hod // 5][hod % 5])[:1]
            if xy.isdigit():
                pole[hod // 5][hod % 5] = players[ch % 2]
            else:
                print('Там занято!')
                ch -= 1
    for i in pole:
        string = ''
        for j in i:
            string += j + '|'
        print(string[:-1])
    if pole[0][0] == pole[0][1] == pole[0][2] == pole[0][3] == pole[0][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[0][0] == pole[0][1] == pole[0][2] == pole[0][3] == pole[0][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break

    if pole[0][0] == pole[0][1] == pole[0][2] == pole[0][3] == pole[0][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[1][0] == pole[1][1] == pole[1][2] == pole[1][3] == pole[1][4] and pole[0][0] == 'X ' or pole[1][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[2][0] == pole[2][1] == pole[2][2] == pole[2][3] == pole[2][4] and pole[0][0] == 'X ' or pole[2][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[3][0] == pole[3][1] == pole[3][2] == pole[3][3] == pole[3][4] and pole[0][0] == 'X ' or pole[3][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[4][0] == pole[4][1] == pole[4][2] == pole[4][3] == pole[4][4] and pole[0][0] == 'X ' or pole[4][0] == 'O ':
        print('Победили ', pole[0][0])
        break

    if pole[0][0] == pole[1][0] == pole[2][0] == pole[3][0] == pole[4][0] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[0][0] == pole[1][1] == pole[2][2] == pole[3][3] == pole[4][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[0][0] == pole[1][1] == pole[2][2] == pole[3][3] == pole[4][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[0][0] == pole[1][1] == pole[2][2] == pole[3][3] == pole[4][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    if pole[0][0] == pole[1][1] == pole[2][2] == pole[3][3] == pole[4][4] and pole[0][0] == 'X ' or pole[0][0] == 'O ':
        print('Победили ', pole[0][0])
        break
    ch += 1
    if ch == 25:
        print('Ничья !')
        break