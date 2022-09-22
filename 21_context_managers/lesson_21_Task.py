import unittest


# task 1
class MyOpen:
    counter = 0

    def __init__(self, file_name, method):
        try:
            self.file_obj = open(file_name, method)
        except FileNotFoundError:
            raise

    def __enter__(self):
        MyOpen.counter += 1
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exception has been handled,"
              f" number of context os {self.counter}")
        self.file_obj.close()
        return True


# task 2
class TestMyOpen(unittest.TestCase):

    def test_counter(self):
        with MyOpen('my_open_module.txt', 'w'):
            ...
        self.assertEqual(MyOpen.counter, 1)
        with MyOpen('my_open_module.txt', 'w'):
            ...
        with MyOpen('my_open_module.txt', 'w'):
            ...
        with MyOpen('my_open_module.txt', 'w'):
            ...
        self.assertEqual(MyOpen.counter, 4)

    def test_with_open(self):
        with MyOpen('my_open_module.txt', 'w') as file:
            file.write('test')
            self.assertEqual(file.readline(), 'test')

    def test_bed_open(self):
        with self.assertRaises(FileNotFoundError):
            MyOpen('my_open_modu.txt', 'r')


# task 3 (optional)
# def text_redactor(file_obj: str):
#     with open(file_obj, 'r+') as file:
#         file_ = file.read()
#         print(type(file))
#         text = file_.strip()
#         for i in text:
#             i.lower()
#         file.write(i)
#
#
# text_redactor('text_redactor_21')


# start
def main():
    # task 1
    with MyOpen('my_open_module.txt', 'a+'):
        ...
    with MyOpen('my_open_module.txt', 'a+'):
        ...
    with MyOpen('my_open_module.txt', 'a+'):
        ...
    # task 2
    # unittest.main()
    # task 3 (optional)
    ...


if __name__ == '__main__':
    main()