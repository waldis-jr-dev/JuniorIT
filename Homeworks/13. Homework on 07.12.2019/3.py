import random
num = int(input('Enter number: '))
a = []
b = []
for i in range(num):
 for u in range(i):
  ran = random.randint(10, 777)
  b.append(ran)
 a.append(b)
 b = []
print(a)