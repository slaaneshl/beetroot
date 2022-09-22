# task 1
user_list = 'some words to dictionaries words'.split()
user_dict = {}
for word in user_list:
    if word in user_dict:
        user_dict[word] += 1
    else:
        user_dict[word] = 1
print(user_dict)

# task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
whole_stock = []
whole_prices = []
check = 0

for i in stock:
    whole_stock.append(stock[i])
for i in prices:
    whole_prices.append(prices[i])
for i in range(len(whole_prices)):
    check += whole_stock[i] * whole_prices[i]
# print(whole_stock)
# print(whole_prices)
print(f"price of fruits: {int(check)}$")

# task 3
print([(i, i ** 2) for i in range(1, 11)])
# user_list_of_tuple = [(i, i ** 2) for i in range(1, 11)]
# print(type(user_list_of_tuple[0]))
# print(user_list_of_tuple)