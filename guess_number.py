from random import randint

input_number = input('Угадайте число от 1 до 100: ')
number = int(input_number)

num = randint(1, 100)
if num == number:
    print('Отличная интуиция! Вы угадали число :)')
elif num > number:
    print('Ваше число меньше того, что загадано')
else:
    print('Ваше число больше того, что загадано')