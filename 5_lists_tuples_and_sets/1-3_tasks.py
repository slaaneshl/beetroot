import random
# task 1
while True:
    user_num = input('Guess what number was generated between 1'
                     ' and 10?(to quit press "q") = ')
    comp_num = random.randint(1, 10)
    if user_num == "q":
        print("Bye! Have a nice day dude<3")
        break
    if user_num != str(comp_num):
        print(f"Wrong! your number is {user_num}. Generated number is"
              f" {comp_num} ")
    if user_num == str(comp_num):
        print(f'Successful! Generated number is {user_num}')
    else:
        continue
# task 2
acc_name = input('Write your name: ')
acc_age = int(input('Type your age: '))
print(f'Greetings {acc_name}, on your next birthday you’ll be'
      f' {acc_age + 1} years!')
# task 3
count = 1
user_string = input('Type your string: ')
while count < 6:
    user_lst = list(user_string)
    random.shuffle(user_lst)
    print(''.join(user_lst))
    count += 1