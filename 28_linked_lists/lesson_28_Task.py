# node
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data


# task 1
class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data: Node) -> None:
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def __repr__(self) -> str:
        current = self.head
        nodes = []

        while current is not None:
            nodes.append(current.data)
            current = current.next

        return f'{nodes}'

    def search(self, item: int | str) -> bool:
        current = self.head

        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item: int | str) -> None:
        current = self.head
        previous = None

        while True:
            if current.data == item:
                break
            previous, current = current, current.next

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def index(self, item: int) -> int | str:
        current = self.head
        count = -1
        while current is not None:
            count += 1
            if count == item:
                return current.data
            current = current.next

    def slice(self, start: int, stop: int) -> list:
        current = self.head
        count = -1
        nodes = []
        while current is not None:
            count += 1

            if count >= start:
                nodes.append(current.data)

                if count == stop:
                    break

            current = current.next

        return nodes


# task 2
class Stack:
    def __init__(self):
        self.head = None

    def isempty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def push(self, data) -> None:

        if self.head is None:
            self.head = Node(data)

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):

        if self.isempty():
            return None

        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    def mapping(self) -> str:
        iter_node = self.head

        if self.isempty():
            return 'Stack Underflow'

        else:
            while iter_node is not None:
                print(iter_node.data, '->', end=' ')
                iter_node = iter_node.next
            return


# task 3
class Queue:

    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def en_queue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def de_queue(self):

        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None


# start
def main():
    # task 1
    my_list = UnorderedList()
    my_list.add(1)
    my_list.add(33)
    my_list.add(2)
    my_list.add(91)
    my_list.add(144)
    my_list.add(21)
    print(my_list)
    print(my_list.size())
    print(my_list.search(2))
    my_list.remove(33)
    print(my_list)
    print(my_list.index(0))
    print(my_list.slice(2, 3))
    # task 2
    MyStack = Stack()
    MyStack.push(17)
    MyStack.push(27)
    MyStack.push(37)
    MyStack.push(47)
    MyStack.mapping()
    MyStack.peek()
    MyStack.pop()
    MyStack.pop()
    MyStack.mapping()
    MyStack.peek()
    # task 3
    queue = Queue()
    queue.en_queue(17)
    queue.en_queue(27)
    print(queue.front.data)
    print(queue.rear.data)
    queue.de_queue()
    queue.de_queue()
    queue.en_queue(37)
    queue.en_queue(47)
    queue.en_queue(57)
    print(queue.front.data)
    print(queue.rear.data)
    queue.de_queue()
    print(queue.front.data)
    print(queue.rear.data)


if __name__ == '__main__':
    main()