# imports
from collections import deque


# task 1
def reverse_order(_list: [int | str]) -> [int | str]:
    _list = deque(_list)
    result = []

    for i in range(len(_list)-1, -1, -1):
        result += _list.pop()

    return result


# task 2
def balanced(string: str) -> str:
    stack = deque()
    _braces = {'(': ')', '{': '}', '[': ']'}

    for i in string:

        if i in _braces:
            stack.append(i)

        elif len(stack) == 0 or _braces[stack.pop()] != i:
            return 'unbalanced'

    return 'balanced'


# task 3
class Stack:

    stack = []

    def append(self, it):
        return self.stack.append(it)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def search(self, it):
        for item in range(len(self.stack)):
            if it == self.stack[item]:
                return f'Stack element found "{self.stack[item]}"'
        else:
            raise ValueError('No such element exists in the stack')

    def __repr__(self):
        return f'Our steck: {self.stack},' \
               f' quantity of elements {len(self.stack)}'


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def search(self, it):
        for item in range(len(self.queue)):
            if it == self.queue[item]:
                return f'Item found in queue "{self.queue[item]}"'
        else:
            raise ValueError('No such element exists in the queue')

    def __repr__(self):
        return f'Our queue {self.queue},' \
               f' quantity of elements in queue {len(self.queue)}'


# start
def main():
    # task 1
    lst = ['a', 'b', 'd', 'f', 'g']
    print(reverse_order(lst))
    # task 2
    print(balanced('([{(){}[]}])'))
    print(balanced('(){(}]'))
    # task 3
    stack = Stack()
    stack.append(1)
    stack.append(3)
    stack.append('bye')
    print(stack.search(3))
    print(stack)
    stack.pop()
    print(stack)
    # ------------ #
    queue = Queue()
    queue.enqueue(9)
    queue.enqueue(1)
    queue.enqueue('bye')
    print(queue.search(9))
    print(queue)
    queue.dequeue()
    print(queue)


if __name__ == '__main__':
    main()