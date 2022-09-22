# task 1

def writing_file(data):

    with open('my_file.txt', 'w') as file:
        file.write(data)


def reading_file():

    with open('my_file.txt', 'r') as file:
        print(file.read())


user_data = 'Hello file world!\n Hail friend!'

writing_file(user_data)
reading_file()
