# task 1
class Person:

    def __init__(self, firstname: str, lastname: str, age: int, sex: str):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex

    def introduction(self):
        return f'Hail friend, my name is {self.firstname}, and' \
               f' I {self.age} years old.'


class Student(Person):

    def __init__(self, firstname, lastname, age, sex, average_rating, club):
        super().__init__(firstname, lastname, age, sex)
        self.average_rating = average_rating
        self.club = club

    def __repr__(self):
        return (self.firstname + ' ' + self.lastname + ', ' + self.age
                + ', ' + self.average_rating + ', ' + self.club + '.'
                )


class Teacher(Person):

    def __init__(self, firstname, lastname, age, sex, salary, post):
        super().__init__(firstname, lastname, age, sex)
        self.salary = salary
        self.post = post

    def __repr__(self):
        return (self.firstname + ' ' + self.lastname + ', ' + self.age
                + ', ' + self.salary + ', ' + self.post + '.'
                )


# task 2
class Mathematician:

    @staticmethod
    def square_nums(numbers):
        return [i ** 2 for i in numbers]

    @staticmethod
    def remove_positives(numbers):
        return [i for i in numbers if i < 0]

    @staticmethod
    def filter_leaps(numbers):
        return [i for i in numbers if i % 4 == 0]


# task 3
class Product:

    def __init__(self, type_: str, name: str, price: int):
        self.type = type_
        self.name = name
        self.price = price
        self.amount = None


class ProductStore:

    def __init__(self, *args: Product):
        self.all_products = []
        self.income = 0

        for product in args:
            self.product = product
            self.product.amount = 1
            self.all_products.append(product)

    def add(self, product, amount, price_premium=0.3):

        if product in self.all_products:
            product.amount += amount

        else:
            self.all_products.append(product)
            product.price *= (1 + price_premium)
            product.amount = amount

    def set_discount(self, identifier, percent, identifier_type='name'):

        if identifier_type == 'name':
            for prod in self.all_products:

                if prod.name == identifier:
                    prod.price *= (1 - percent / 100)

        elif identifier_type == 'type':
            for prod in self.all_products:

                if prod.name == identifier:
                    prod.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):

        for prod in self.all_products:

            if prod.name == product_name and prod.amount >= amount:
                prod.amount -= amount
                self.income += prod.price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):

        for prod in self.all_products:
            print(prod.name, prod.type, prod.price, prod.amount)

    def get_product_info(self, product_name):
        lst_ = [
            print(prod.__dict__) for prod in self.all_products
            if prod.name == product_name
        ]
        if not lst_:
            raise ValueError('Such product does not exist')


# task 4
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('log_exception.txt', 'a') as file:
            file.write(msg + '\n')
# start


def main():
    # task 1
    student_1 = Student('Jesse', 'Pinkman', "16", 'male',
                        'D-', "Doesn't consist in any clubs")
    teacher_1 = Teacher('Walter', 'White', "50", 'male',
                        "$54,256", 'Chemistry teacher')
    print(student_1.introduction())
    print(student_1, teacher_1)
    # task 2
    m = Mathematician()
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
    # task 3
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product("Ramen", 10)
    # task 4
    raise CustomException('Issue')


if __name__ == '__main__':
    main()
