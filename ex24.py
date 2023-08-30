'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.'''

from random import randint

n = 10
ai = []

for i in range(n):
    ai.append(randint(1,100))

print(f'amount of blueberries on each bush: {ai}')

max = 0

for k in range(len(ai)):
    if k == 0:
        amount = ai[k]+ai[k+1]+ai[len(ai)-1]
        if max < amount: 
            max = amount
    elif k == len(ai)-1:
        amount = ai[k]+ ai[k-1]+ai[len(ai)-k-1]
        if max < amount:
            max = amount
    else:
        amount = ai[k]+ai[k-1]+ai[k+1]
        if max < amount:
            max = amount
    
    
    print(f'center bush is {k}, sum of berries on three bushes: {amount}')

print(f'max berries amount is {max}')


   