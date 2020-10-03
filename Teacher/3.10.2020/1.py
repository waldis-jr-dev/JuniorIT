a = 'ASDF'
ch = 0
upper_symbols = ''
while ch < len(a):
    if a[ch].upper():
        upper_symbols += a[ch]
    ch += 1
ch = 0
upper_ch = 0
upper_symbols = upper_symbols[::-1]
answer = ''
while ch < len(a):
    if a[ch].isupper():
        answer += upper_symbols[upper_ch]
        upper_ch += 1
    else:
        answer += a[ch]
        ch += 1
print(answer)
