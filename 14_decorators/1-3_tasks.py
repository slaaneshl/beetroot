from functools import wraps


# task 1


def logger(function):
    @wraps(function)
    def wrap(*args, **kwargs):
        print(function.__name__, 'called with', *args, **kwargs)

    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


# task 2


def stop_words(words: list):
    def inner(function):
        @wraps(function)
        def wrap(*args, **kwargs):
            txt = function(*args, **kwargs)

            for word in words:
                txt = txt.replace(word, '*')

            return txt

        return wrap

    return inner


@stop_words(['pepsi', 'BMW', 'Leva'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# task 3


def arg_rules(type_: type, max_length: int, contains: list):
    def inner(function):

        @wraps(function)
        def wrap(arguments, *args, **kwargs):

            if not isinstance(arguments, type_):
                print('Error with input')
                return False

            if len(arguments) > max_length:
                print('Error with input')
                return False

            for i in contains:

                if i not in arguments:
                    print('Error with input')
                    return False

            return function(arguments, *args, **kwargs)

        return wrap

    return inner


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan_second(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# start


def main():
    add(4, 5)
    square_all(3, 5, 7)
    print(create_slogan('Leva and Oleg'))
    print(create_slogan_second('05@mail.com'))


if __name__ == '__main__':
    main()
