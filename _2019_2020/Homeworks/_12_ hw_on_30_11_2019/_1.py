a = input('stroka: ') + '$'

sign_place = 0

for i in range(len(a)):
    if a[i] in '*+-/':
        sign_place = i
        break

answ = float(a[:sign_place])
i = sign_place

for j in range(i+1, len(a)):
    if a[j] in '*+-/$':
        if a[sign_place] == '+' or (a[j] == '$' and a[sign_place] == '+'):
            answ += float(a[sign_place+1:j])
            sign_place = j

        elif a[sign_place] == '-' or (a[j] == '$' and a[sign_place] == '-'):
            answ -= float(a[sign_place+1:j])
            sign_place = j

        elif a[sign_place] == '*' or (a[j] == '$' and a[sign_place] == '*'):
            answ *= float(a[sign_place+1:j])
            sign_place = j

        elif a[sign_place] == '/' or (a[j] == '$' and a[sign_place] == '/'):
            if float(a[sign_place+1:j]) != 0:
                answ /= float(a[sign_place+1:j])
            else:
                answ /= 1
                print('Ty zatupil j delil na nol')
            sign_place = j

print(answ)



