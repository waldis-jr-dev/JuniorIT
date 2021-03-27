phone = input('Enter phone: ')
first = phone[0]
last = phone[1:len(phone):1]

if len(phone) == 13 and  first == '+' and last.isdigit() :
    print('Number correct')
else:
    print('Number incorrect')
