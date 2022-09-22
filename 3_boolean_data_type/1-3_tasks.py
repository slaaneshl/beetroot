import os
# task 1
name = "Trevor"
day = 'Saturday'
language = 'python'
print(f"Good day {name}!", day.upper(), "is a perfect day to learn some %s." % language)
# task 2
user_name = os.getlogin()
real_name = 'leva'
print("name of computer: " + user_name + ', ' + 'real name: ' + real_name)
# task 3
x = 9
y = 6
print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x ** y)
print(x // y)
print(x % y)