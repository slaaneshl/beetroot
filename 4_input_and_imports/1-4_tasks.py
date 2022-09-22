# task 1
string = 'hail friend'
num = len(string)
if num > 2:
    print(string[:2] + string[-2:])
else:
    num = None
    print('empty')
# task 2
phone_number = '0234921571'
phone_len = len(phone_number)
if phone_number.isdigit():
    if phone_len == 10:
        print(f'Number +{phone_number} - is correct ')
    else:
        print("wrong amount")
else:
    print('invalid symbols')
# task 3
expression = 6+7
math_answer = int(input('6+7='))
if math_answer == expression:
    print('your right')
else:
    print('wrong answer')
# task 4
name = 'leva'.lower()
check = input('Write your name: ').lower()
if check == name:
    print(f'Greetings {name.title()}')
else:
    print('Wrong name')
