from functools import wraps


# task 1
class Email:
    def __init__(self, email: str):
        self.email = email

    def validate(self):
        symbols = ['@', '.com']
        if isinstance(self.email, str):

            if len(self.email) < 26:

                if all([symbol in self.email for symbol in symbols]):
                    return 'Your email is correct'

                else:
                    raise NameError('Stick to the example: "example@mail.com"')
            else:
                raise ValueError("can't be more than 25 symbols")
        else:
            raise TypeError('must be sting!')


# task 2
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __str__(self):
        return f'Boss info --- ' \
               f'id: {self.id}; name: {self.name}; company: {self.company}; ' \
               f'workers list: {self.workers}'

    def __repr__(self):
        return self.__str__()


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def __str__(self):
        return f'\n --Worker info = ' \
               f'id: {self.id}; name: {self.name}; company: {self.company}; ' \
               f'BOSS - {self.boss.name}.--'

    def __repr__(self):
        return self.__str__()


# task 3


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrap(*args):
            return int(*args)
        return wrap

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrap(*args):
            return bool(*args)

        return wrap

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrap(*args):
            return float(*args)
        return wrap


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_anything(string: str):
    return string


# start
def main():
    # task 1
    user_email = Email('lbezver21@gmail.com')
    print(user_email.validate())
    # task 2
    nick = Boss(3, 'Nick', 'Google')
    sasha = Worker(21, 'Sasha', 'Google', nick)
    nick.workers = Worker(284, 'Bogdan', 'Google', nick)
    nick.workers = Worker(33, 'Alex', 'Google', nick)
    nick.workers = Worker(sasha.id, sasha.name, sasha.company, nick)
    print(nick)
    # task 3
    assert do_nothing('25') == 25
    assert do_something('True') is True


if __name__ == '__main__':
    main()
