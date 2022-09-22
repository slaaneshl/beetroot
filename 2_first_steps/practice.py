import os
name = os.getlogin()
solution = input('dodik or clown')
with open('cringe_moment', 'a') as file:
    if solution == '1':
        print('dodik', name, file=file)
    else:
        print('clown')
