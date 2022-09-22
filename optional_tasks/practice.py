# class Person:
#
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#
#     def talk(self):
#         print(f'Hello, my name is {self.firstname + " " + self.lastname} and'
#               f' I’m {self.age} years old!')
#
#
# me = Person('Lev', 'Bezverkhniy', 18)
# print(me.talk())
# class Dog:
#     age_factor = 7
#
#     def __init__(self, age):
#         self.age = age
#
#     def human_age(self):
#         return self.age * self.age_factor
#
#
# shibe = Dog(4)
# print(shibe.human_age())
# class TVController:
#     num_channel = 0
#
#     def __init__(self, channels: list) -> list:
#         self.channels = channels
#
#     def start(self):
#         return self.channels[self.num_channel - 1]
#
#     def first_channel(self):
#         self.num_channel = 0
#         return self.channels[self.num_channel]
#
#     def last_channel(self):
#         self.num_channel = -1
#         return self.channels[self.num_channel]
#
#     def turn_channel(self, N):
#         try:
#             self.num_channel = N
#             return self.start()
#
#         except IndexError:
#             return f' channel {N} not in list'
#
#         except TypeError:
#             return f'"{N}", wrong type'
#
#     def next_channel(self):
#
#         if self.num_channel < 0:
#             self.num_channel = 0
#             return self.channels[self.num_channel]
#
#         if self.num_channel == len(self.channels):
#             self.num_channel = 0
#             return self.channels[self.num_channel]
#
#         if self.num_channel < len(self.channels):
#             self.num_channel = self.num_channel + 1
#             return self.start()
#
#     def previous_channel(self):
#
#         if self.num_channel == -len(self.channels):
#             self.num_channel = -1
#             return self.channels[self.num_channel]
#
#         if self.num_channel < 0:
#             self.num_channel -= 1
#             return self.channels[self.num_channel]
#
#         if self.num_channel == 0:
#             self.num_channel = -1
#             return self.channels[self.num_channel]
#
#         else:
#             self.num_channel = self.num_channel - 1
#             return self.start()
#
#     def current_channel(self):
#         return self.channels[self.num_channel]
#
#     def is_exist(self, N):
#         if isinstance(N, int):
#             if N - 1 < len(self.channels):
#                 return 'Yes'
#             else:
#                 return 'No'
#
#         if isinstance(N, str):
#             if N in self.channels:
#                 return 'Yes'
#             else:
#                 return 'No'
#
#
# custom_channels = ["BBC", "Discovery", "TV1000"]
# controller = TVController(custom_channels)
# print(controller.first_channel())
# print(controller.last_channel())
# print(controller.turn_channel(1))
# print(controller.next_channel())
# print(controller.previous_channel())
# print(controller.current_channel())
# print(controller.is_exist(3))
# print(controller.current_channel())


# class Author:
#     def __init__(self, name, country, birthday, books):
#         self.name_author = name
#         self.country_author = country
#         self.birthday_author = birthday
#         self.books_author = books
#
#     def __str__(self):
#         return f"{self.name_author}, was born in {self.country_author} " \
#                f"on {self.birthday_author}"
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Book:
#     def __init__(self, name, year, authors: Author):
#         self.name_book = name
#         self.year_book = year
#         self.author_book = authors
#
#     def __str__(self):
#         return f'{self.name_book} written {self.year_book} auther ' \
#                f'{self.author_book.name_author}'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.authors = []
#
#     def new_book(self, name: Book, year: Book, author: Author):
#         self.books.append((name, year))
#         self.authors.append(author.name_author)
#
#     def group_by_author(self, author: Author):
#         ...
#
#     def group_by_year(self, year: int):
#         ...
#
#     def __str__(self):
#         return f'{self.name} Has {self.books} of authors {self.authors}'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name.title()
#         self.last_name = last_name.title()
#
#     @property
#     def full_name(self):
#         return self.first_name.title() + ' ' + self.last_name.title()
#
#     @property
#     def initials(self):
#         return self.first_name[0].upper() + self.last_name[0].upper()
#
#     @full_name.setter
#     def full_name(self, name):
#         first, last = name.split(' ')
#         self.first_name = first.title()
#         self.last_name = last.title()
#
#     @full_name.deleter
#     def full_name(self):
#         self.first_name = None
#         self.last_name = None
#         print('deleted')
#
#
# LF = Person('Lev', 'Falko')
# print(LF.last_name, LF.first_name)
# print(LF.full_name)
# print(LF.initials)
# print('-----------------')
# LF.first_name = 'clown'
# print(LF.last_name, LF.first_name)
# print(LF.full_name)
# print(LF.initials)
# print('-----------------')
# LF.full_name = 'Kolya Ysenivskiy'
# print(LF.last_name, LF.first_name)
# print(LF.full_name)
# print(LF.initials)
# print('-----------------')
# del LF.full_name
# print(LF.last_name, LF.first_name)
# from functools import wraps
#
#
# class TypeDecorators:
#
#     @staticmethod
#     def to_int(func):
#         @wraps(func)
#         def inner(*args):
#
#             return int(func(*args))
#
#         return inner
#
#
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
#
#
# print(type(do_nothing('25')))
#
# assert do_nothing('25') == 25
# def main():
#     prod1 = Product('T-shirt', 200, 20)
#     prod2 = Product('Hoodie', 800, 7)
#     storage1 = ProductStorage()
#     storage1.add_to_storage(prod1)
#     storage1.add_to_storage(prod2)
#     cart1 = ShoppingCart(storage1)
#     cart1.add_item('T-shirt', 2)
#     cart1.add_item('Hoodie', 3)
#     cart1.payment_receipt()
#     print(cart1.p_storage.storage)
#
#
# if __name__ == '__main__':
#     main()

# import json
#
#
# class Product:
#     item_id = 0
#
#     def __init__(self, prod_name, prod_price_uah, prod_amount):
#         self.prod_name = prod_name
#         self.prod_price_uah = prod_price_uah
#         self.prod_amount = prod_amount
#         Product.item_id += 1
#
#     def product_return(self):
#         product = {
#                     'name': self.prod_name,
#                     'amount': self.prod_amount,
#                     'price_uah': self.prod_price_uah,
#                     'id': self.item_id
#
#                 }
#         return product
#
#     def __str__(self):
#         return f'{self.__class__.__name__} name: {self.prod_name} - ' \
#                f'{self.prod_amount} pcs ({self.prod_price_uah} UAH per each)'
#
#     def __repr__(self):
#         return self.__str__()
#
#
# class ProductStorage:
#     @staticmethod
#     def add_to_storage(product: Product):
#         item = {
#             'name': product.prod_name,
#             'amount': product.prod_amount,
#             'price_uah': product.prod_price_uah,
#             'id': product.item_id
#         }
#         with open('storage.json', 'r') as file:
#             loaded_file = json.load(file)
#             loaded_file.append(item)
#
#             with open('storage.json', 'w') as file2:
#                 json.dump(loaded_file, file2, indent=4)
#
#     @staticmethod
#     def delete_from_storage(item_id: int):
#         with open('storage.json', 'r') as file:
#             loaded_file = json.load(file)
#             for i in loaded_file:
#                 if i['id'] == item_id:
#                     del i
#             with open('storage.json', 'w') as file2:
#                 json.dump(loaded_file, file2, indent=4)
#
#
# class ShoppingCart:
#     name = None
#     amount = 0
#     cart = []
#
#     def add_item(self, item_id):
#         with open('storage.json', 'r') as file:
#             for i in file:
#
#                 if i['id'] == item_id:
#                     self.cart.append(i)
#
#     @staticmethod
#     def delete_item(item_id, amount):
#         with open('storage.json', 'a') as file:
#             for i in file:
#                 if i['id'] == item_id:
#
#                     if i['amount'] == amount:
#                         del i
#
#                     else:
#                         ...
#
#     def payment_receipt(self):
#         ...
#
#     def __str__(self):
#         return f'{self.__class__.__name__}'
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}'
#
#
# def main():
#     # item1 = Product('sss', 27, 12)
#     # ProductStorage.add_to_storage(item1)
#     # ProductStorage.delete_from_storage(1)
#     ...
#
#
# if __name__ == "__main__":
#     main()
#
# class Duck:
#     def __init__(self, name: str) -> str:
#         self.name = name
#
#     def walk(self):
#         return f'duck {self.name}: *walking across beach.'
#
#     def voice(self):
#         return f'duck {self.name}: quack, quack, quack!'
#
#
# my_duck = Duck('Issac')
# print(my_duck.walk())
# print(my_duck.voice())

# from dataclasses import dataclass, field
# from decimal import Decimal
# from uuid import uuid4
#
#
# @dataclass
# class Product:
#     name: str
#     price: Decimal
#     amount: int = 1
#     sku: str = field(default_factory=uuid4)
#
#
# milk = Product("Village", "34.19", 40)
# print(milk)

# lst = ['a', 'b', 'd', 'f', 'g']
#
# for i in range(len(lst)):
#     print(lst[i])
# print('############')
# for i in range(len(lst)-1, -1, -1):
#     print(lst[i])

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return self.data
#
#
# class LinkedList:
#
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next
#
#     def add_first(self, node):
#         node.next = self.head
#         self.head = node
#
#     def add_last(self, node):
#         if self.head is None:
#             self.head = node
#             return
#         for current_node in self:
#             pass
#         current_node.next = node
#
#     def add_before(self, target_node_data, new_node):
#         if self.head is None:
#             raise Exception("List is empty")
#
#         if self.head.data == target_node_data:
#             return self.add_first(new_node)
#
#         prev_node = self.head
#         for node in self:
#             if node.data == target_node_data:
#                 prev_node.next = new_node
#                 new_node.next = node
#                 return
#             prev_node = node
#
#         raise Exception("Node with data '%s' not found" % target_node_data)
#
#     def remove_node(self, target_node_data):
#         if self.head is None:
#             raise Exception("List is empty")
#
#         if self.head.data == target_node_data:
#             self.head = self.head.next
#             return
#
#         previous_node = self.head
#         for node in self:
#             if node.data == target_node_data:
#                 previous_node.next = node.next
#                 return
#             previous_node = node
#
#         raise Exception("Node with data '%s' not found" % target_node_data)
#
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)
#
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
#
#
# class Node:
#     def __init__(self, data=None) -> None:
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return self.data
#
#
# class UnorderedList:
#     def __init__(self, nodes=None):
#         self.head = None
#         if nodes is not None:
#             node = Node(data=nodes.pop(0))
#             self.head = node
#             for elem in nodes:
#                 node.next = Node(data=elem)
#                 node = node.next
#
#     def is_empty(self):
#         return self.head is None
#
#     def add(self, node: Node):
#         if self.head is not None:
#             self.head = node
#             return
#         for current in self:
#             pass
#
#         current.next = node
#
#     def __repr__(self):
#         node = self.head
#         nodes = []
#
#         while node:
#             nodes.append(node.data)
#             node = node.next
#
#         nodes.append('None')
#         return ' -> '.join(nodes)
#
#     def __iter__(self):
#         node = self.head
#         while node is not None:
#             yield node
#             node = node.next
#
#
# mylist = UnorderedList()
# mylist.add(Node('21'))
# mylist.add(Node('34'))
# mylist.add(Node('1'))
# print(mylist)

# def selection_sort(array: list[int]) -> None:
#
#     for i in range(len(array) - 1):
#         min_value = array[i]
#         min_value_index = i
#
#         for j in range(i + 1, len(array)):
#
#             if min_value > array[j]:
#                 min_value = array[j]
#                 min_value_index = j
#
#         if min_value_index != i:
#             temp = array[i]
#             array[i] = array[min_value_index]
#             array[min_value_index] = temp
#
#
# lst = [3, 5, 2, 8, 1, 6, 9, 0, 4, 7]
# selection_sort(lst)
# print(lst)
# from collections import deque
#
# graph = {'me': ['oleg', 'kolya', 'sveta'],
#          'oleg': ['lina', 'tanya', 'ruslan'],
#          'lina': ['tanya'],
#          'tanya': ['lina', 'ruslan'],
#          'ruslan': ['lina', 'tanya'],
#          'kolya': ['pasha', 'vitalik', 'sveta'],
#          'pasha': [],
#          'vitalik': [],
#          'sveta': ['kolya', 'andrey', 'oleg'],
#          'andrey': []}
#
#
# def first_latter_in_graph(name):
#     return name.startswith('t')
#
#
# def search_graph(user_graph: dict) -> str:
#     search_queue = deque()
#     search_queue += user_graph
#     done_list = []
#     counter = 0
#     while search_queue:
#
#         person_name = search_queue.popleft()
#         if person_name not in done_list:
#             counter += 1
#             if first_latter_in_graph(person_name):
#                 return f' name: {person_name} \n counter: {counter}'
#             else:
#                 search_queue += graph[person_name]
#                 done_list.append(person_name)
#     return 'fail'
#
#
# print(search_graph(graph['me']))

# import sys
#
# from PyQt5.QtWidgets import (QApplication,
#                              QWidget,
#                              QLabel,
#                              QPushButton,
#                              QLineEdit,
#                              QComboBox,
#                              QRadioButton,
#                              QHBoxLayout,
#                              QVBoxLayout,
#                              QGridLayout,
#                              QFormLayout,
#                              QDialog,
#                              QDialogButtonBox,
#                              QMainWindow,
#                              QToolBar,
#                              QStatusBar
#                              )
#

# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('hello world')
# window.setGeometry(50, 50, 300, 300)
#
# message = QLabel('<h1>Hello World</h1>', parent=window)
# message.move(50, 50)
#
# button = QPushButton('click', parent=window)
# button.move(50, 100)
#
# edit = QLineEdit('', parent=window)
# edit.move(50, 150)
#
# combo = QComboBox(parent=window)
# combo.addItems(['python', 'java', 'go', 'java script'])
# combo.move(200, 50)
#
# radio = QRadioButton('python', parent=window)
# radio.move(200, 150)
#
# window.show()
#
# sys.exit(app.exec_())
# 1. horizontal layout
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('horizontal / Vertical')
#
# # layout_h = QHBoxLayout()
# # layout_h.addWidget(QPushButton('left', parent=window))
# # layout_h.addWidget(QPushButton('middle', parent=window))
# # layout_h.addWidget(QPushButton('right', parent=window))
# # layout_h.addWidget(QLabel('bye', parent=window))
# #
# # window.setLayout(layout_h)
#
# layout_v = QVBoxLayout()
# layout_v.addWidget(QPushButton('top', parent=window))
# layout_v.addWidget(QPushButton('center', parent=window))
# layout_v.addWidget(QPushButton('bottom', parent=window))
# layout_v.addWidget(QLabel('bye', parent=window))
#
# window.setLayout(layout_v)
#
# window.show()
#
# sys.exit(app.exec_())\

# 2. Grid
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Grid')
#
# layout = QGridLayout()
#
# layout.addWidget(QPushButton('button'), 0, 0)
# layout.addWidget(QPushButton('button'), 0, 1)
# layout.addWidget(QPushButton('button'), 0, 2)
# layout.addWidget(QPushButton('button'), 1, 0)
# layout.addWidget(QPushButton('button'), 1, 1)
# layout.addWidget(QPushButton('button'), 1, 2)
# layout.addWidget(QPushButton('button'), 2, 0)
# layout.addWidget(QPushButton('button'), 2, 1, 1, 2)
#
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec_())

# From layout
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle('Grid')
#
# layout = QFormLayout()
# layout.addRow('Name', QLineEdit())
# layout.addRow('Age', QLineEdit())
# layout.addRow('Education', QLineEdit())
# layout.addRow('Job', QLineEdit())
# layout.addRow('Hobbies', QLineEdit())
# layout.addWidget(QPushButton('Submit'))
#
# window.setLayout(layout)
#
# window.show()
# sys.exit(app.exec_())
# class Dialog(QDialog):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle('Dialog window')
#         box_layout = QVBoxLayout()
#         form_layout = QFormLayout()
#
#         form_layout.addRow('Name', QLineEdit())
#         form_layout.addRow('Age', QLineEdit())
#         form_layout.addRow('Education', QLineEdit())
#         form_layout.addRow('Job', QLineEdit())
#         form_layout.addRow('Hobbies', QLineEdit())
#
#         box_layout.addLayout(form_layout)
#
#         buttons = QDialogButtonBox()
#
#         buttons.setStandardButtons(QDialogButtonBox.No |
#                                    QDialogButtonBox.Ok)
#         box_layout.addWidget(buttons)
#         self.setLayout(box_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = Dialog()
#     dialog.show()
#     app.exec_()
#
# class MyWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle('My Window')
#         self.setCentralWidget(QLabel('Central title'))
#         self._create_menu()
#         self._create_tool_()
#
#     def _create_menu(self):
#         self.menu = self.menuBar().addMenu('Menu')
#         self.menu.addMenu('edit')
#         self.menu.addAction('Exit', self.close)
#         self.menu.addAction('Change size', self.adjustSize)
#
#     def _create_tool_(self):
#         tools = QToolBar()
#         self.addToolBar(tools)
#         tools.addAction('Exit', self.close)
#
#     def _create_status_bar(self):
#         status = QStatusBar()
#         status.showMessage('some massage')
#         self.setStatusBar(status)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.setGeometry(50, 50, 300, 300)
#     window.show()
#     app.exec_()

# Signals
# def greeting():
#     if message.text():
#         message.setText('')
#     else:
#         message.setText('Hi')
#
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('Signals')
#
# layout = QVBoxLayout()
# button = QPushButton('Greetings')
#
# button.clicked.connect(greeting)
#
# layout.addWidget(button)
# message = QLabel('')
# layout.addWidget(message)
#
# window.setLayout(layout)
#
# window.show()
# app.exec_()
#########################################
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
time.sleep(5)
print(current_time)
