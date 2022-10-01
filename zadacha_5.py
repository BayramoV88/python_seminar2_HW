# Реализуйте алгоритм перемешивания списка.

import random
num = [1, 2, 3, 4, 5]
print(f'Исходный список {num}')

for i in range(len(num)-1, 0, -1):
    j = random.randint(0, i)
    num[i], num[j] = num[j], num[i]
print(f'Перемешанный список {num}')