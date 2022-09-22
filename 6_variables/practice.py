# user_list = [21, 69, 322, 228, 666, 81, 777, 999, 505, 47, 96]
# print(user_list)
# new_number = int(input('place your number into list: '))
# user_list.append(new_number)
# print(user_list)
# range_len = 10
# range_obj = range(range_len)
# i = 1
# while i < range_len:
#     print(range_obj[i])
#     i += 1
# s2 = {1, 2, 5, 7, 4, 2, 6, 3, 1}
# print(s2)
# s3 = set([1, 2, 3, 7, 4])
# print(s3)
# a = {2, 4, 6}
# b = {2, 5, 7}
# print(a - b)
# print((a - b) == a.difference(b))
# s4 = frozenset((1, 4, 2, 6))
# print(s4)
# x = [2, 5, 9, 3]
# print(id(x))
# x.append(5)
# print(id(x))
# y = (2, 5, 3)
# print(id(y), y)
# y = y + (1,)
# print(id(y), y)
# while True:
#     user_input = input('write some numbers: ')
#     if not user_input.isdigit():
#         print("it is not a number ")
#         continue
#     print(user_input)
# food_list = ['bob', 'apple', 'Milk', 'bread', 'Water']
# food_list.sort(key=str.lower)
# print(food_list)

# import random
#
#
# def random_number():
#     return random.randint(1, 101)
#
#
# comp_list_1 = []
# comp_list_2 = []
# count = 1
# while count < 11:
#     comp_list_1.append(random_number())
#     comp_list_2.append(random_number())
#     count += 1
#
# comp_sets_1 = set(comp_list_1)
# comp_sets_2 = set(comp_list_2)
# comp_list_3 = list(comp_sets_1.intersection(comp_sets_2))
#     if comp_list_3 == None:
#         print('no matches')
#
# print(comp_list_3)
# s = ([1, 2, 3], [0, 1], [['four'] * 4])
# print(len(s))

# lst = []
# for i in range(0,101):
#     if i % 7 == 0 and i % 5 != 0:
#         lst.append(i)
#         print(lst)
# lst = []
# i = 0
# while i < 100:
#     if i % 7 == 0 and i % 5 != 0:
#         lst.append(i)
#         print(lst)
#     i += 1