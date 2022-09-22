# task 1
def oops():
    raise IndexError
    # raise KeyError


try:
    oops()

except IndexError:
    print('ERROR with the index')

# task 2
while True:
    try:
        a = int(input('first number: '))
        b = int(input('second number: '))

        result = a ** 2 / b
        print(result)

    except ValueError:
        print('It isn\'t a number')
        continue

    except ZeroDivisionError:
        print('Can\'t be divided by zero')
        continue

    break