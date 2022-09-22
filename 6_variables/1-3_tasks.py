# task 1
import random


def random_number():
    return random.randint(1, 100)


user_list = []

while len(user_list) < 11:
    user_list.append(random_number())

print(user_list)
print(max(user_list))
# # task 2

comp_list_1 = []
comp_list_2 = []
count = 1

while count < 11:
    comp_list_1.append(random_number())
    comp_list_2.append(random_number())
    count += 1

comp_sets_1 = set(comp_list_1)
comp_sets_2 = set(comp_list_2)
comp_list_3 = list(comp_sets_1.intersection(comp_sets_2))
print(comp_list_3)
# task 3
lst = []
i = 0
while i < 100:
    if i % 5 != 0:
        lst.append(i)
    i += 7
print(lst)
