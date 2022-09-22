# task 1
class Person:

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.firstname + ' ' + self.lastname} " \
               f"and I’m {self.age} years old!"


# task 2
class Dog:
    age_factor = 7

    def __init__(self, age: int) -> int:
        self.age = age

    def human_age(self):
        return self.age * self.age_factor


# task 3
class TVController:
    num_channel = 0

    def __init__(self, channels: list) -> list:
        self.channels = channels

    def start(self):
        return self.channels[self.num_channel - 1]

    def first_channel(self):
        self.num_channel = 0
        return self.channels[self.num_channel]

    def last_channel(self):
        self.num_channel = -1
        return self.channels[self.num_channel]

    def turn_channel(self, N):
        try:
            self.num_channel = N
            return self.start()

        except IndexError:
            return f'channel {N} not in list'

        except TypeError:
            return f'"{N}", wrong type'

    def next_channel(self):

        if self.num_channel < 0:
            self.num_channel = 0
            return self.channels[self.num_channel]

        if self.num_channel == len(self.channels):
            self.num_channel = 0
            return self.channels[self.num_channel]

        if self.num_channel < len(self.channels):
            self.num_channel = self.num_channel + 1
            return self.start()

    def previous_channel(self):

        if self.num_channel == -len(self.channels):
            self.num_channel = -1
            return self.channels[self.num_channel]

        if self.num_channel < 0:
            self.num_channel -= 1
            return self.channels[self.num_channel]

        if self.num_channel == 0:
            self.num_channel = -1
            return self.channels[self.num_channel]

        else:
            self.num_channel = self.num_channel - 1
            return self.start()

    def current_channel(self):
        return self.channels[self.num_channel]

    def is_exist(self, N):
        if isinstance(N, int):
            if N - 1 < len(self.channels):
                return 'Yes'
            else:
                return 'No'

        if isinstance(N, str):
            if N in self.channels:
                return 'Yes'
            else:
                return 'No'


custom_channels = ["BBC", "Discovery", "TV1000"]
controller = TVController(custom_channels)

# start


def main():
    # task 1
    me = Person('Lev', 'Bezverkhniy', 18)
    print(me.talk())
    # task 2
    shibe = Dog(3)
    print(shibe.human_age())
    # task 3
    print(controller.first_channel())
    print(controller.last_channel())
    print(controller.turn_channel(1))
    print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.current_channel())
    print(controller.is_exist(3))
    print(controller.current_channel())


if __name__ == '__main__':
    main()