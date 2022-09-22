# 1 task
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]
# list3 = list(set(list1) & set(list2))
# print(list3)
# 2 task
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]
# list3 = list(set(list1+list2))
# 3 task
# price = [1.09, 23.56, 57.84, 4.56, 6.78]
# lst = []
# TAX_RATE = 0.2
# for i in price:
#     price.append((i * TAX_RATE) + i)
# print(price)
# 4 task
# from string import punctuation
#
#
# sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'
# print([i for i in sentence if i in 'euioa'])
# print([i for i in sentence if i not in 'euioa' and i.isalpha()])
# print(punctuation)

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# lst = []
# print([lst.append("it's a gift") for i in original_prices if i < 0])

# quote = "If I were married to you, I'd put poison in your coffee. If I were married to you, I'd drink it."
# print({i for i in quote if i in 'euioa'})

# Task8
#
# Виведіть на екран словник у якого ключі будуть числа від 1 до 10, а значення це число у кубі
# Додаткова умова ключі повинні бути не числами а строками 1 - це 'один', 2 - 'два' і т.д.


# print({key:idx ** 3 for idx, key in enumerate(keys) })
# alp_ = {
#     1: 'one'
#     2: 'two'
#     3: 'three'
# }

# Task9
#
# Створіть просту матрицю 5 на 5 з випадкових чисел у диапазоні від -9 до 9
# Виведіть красиво на екран
# import random
# from pprint import pprint
#
# matrix = [random.sample(range(-9, 10), 5) for _ in range(5)]
# pprint(matrix)
# lst = []
# print([lst.append(i) for i in matrix])
#
# element = [i for i in range(-6, 6)]
# matrix = [element for o in range(5)]
# print([element for row in matrix for element in row])
#
# digits = [1, 4, 6, 7, 4, 1, 12, 3, 7, 18]
# print([i for i in digits ])
# words = ['cat', 'window', 'defenestrate']
# for w in words[:]:  # Loop over a slice copy of the entire list.
#     if len(w) > 6:
#         words.insert(0, w)
# print(words)

# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#         else:
#             # loop fell through without finding a factor
#             print(n, 'is a prime number')

# names = {'leva': 1488,
#          'Nicolay': 7777,
#          'Oleg': 9999}
# print(names)
# names['Olha'] = 1111
# print(names)
# del names['Oleg']
# print(names)
# print(list(names))
# print(sorted(names))
# print('leva' in names)
# sss = dict([('leva', 1488), ('Nicolay', 7777), ('Oleg', 9999)])
# print(sss)
# print(names['leva'])

# lst = [x**2 for x in range(1, 13) if x % 3 != 0]
# print(lst)
# vec = [-4, -2, 0, 2, 4]
# print([x**2 for x in vec])
# dicte = {666: 'six six six',
#          777: 'seven seven seven'}
# x = dicte.get(665, 'fuck u')
# print(x)

# res = [x for x in range(0,600, 6) if x % 7 == 0]
# print(res)
temp = []
for i in range(0, 10):
    if i % 2:
        continue
    temp.append(i)
print(sum(temp))