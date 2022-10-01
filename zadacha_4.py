# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

from random import Random, randint
N = int(input('Введите число \n'))
num = []
for i in range(N):
    num.append(randint(-N,N+1))
print(num)

a = int(input('Введите позицию числа a \n'))
b = int(input('Введите позицию числа b \n'))
proizvedenie = 1

if N > a and N > b:
    for i in range(len(num)):
        proizvedenie = num[a - 1] * num[b - 1]
    print(f'Произведение чисел {num [a - 1]} и {num[b -1]} =', proizvedenie)
else:
    print('Такой позиции числа a или b не существует')

#if N > a and N > b:
 #   proizvedenie = num(a) * num (b)
#else:
 #   print('Такого a или b не существует')
# print(proizvedenie)