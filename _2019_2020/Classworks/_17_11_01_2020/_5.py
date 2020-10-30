def gls(str1):
    t = 0
    gls = 'AEIOUaeiou'
    for i in str1:
        if i in gls:
            t += 1
    print(t)


str1 = input('Enter string: ')
gls(str1)