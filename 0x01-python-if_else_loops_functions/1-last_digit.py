#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldig = abs(number) % 10
if number < 0:
    ldig *= -1
print('Last digit of {} is {}'.format(number, ldig), end=' ')
if ldig > 5:
    print ('and is greater than 5')
elif ldig == 0:
    print('and is 0')
elif ldig < 6 and ldig != 0:
    print('and is less than 6 and not 0')
