# task 1
def with_index(iterable, start=1):
    _index = 0
    while start < len(iterable):
        yield start, iterable[_index]
        start += 1
        _index += 1


# task 2
def in_range(start, end, step=1):
    while start < end:
        yield start
        start += step


# task 3
class Iterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable)-1:
            self.index += 1
            return self.iterable[self.index]
        raise StopIteration


class Iterable:
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        return Iterator(self.list_)

    def __getitem__(self, key):
        return self.list_[key]


# start
def main():
    # task 1
    l1 = ['cheese', 'bread', 'lemon', 'juice', 'milk']
    generator1 = with_index(l1)
    for i in generator1:
        print(i)
    # task 2
    generator2 = in_range(1, 76, 5)
    for i in generator2:
        print(i)
    # task 3
    generator3 = Iterable([9, 21, 33])
    for i in generator3:
        print(i)
    ...


if __name__ == '__main__':
    main()