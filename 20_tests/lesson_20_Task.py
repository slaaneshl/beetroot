import unittest
from lesson_15_Task import Dog


# task 1
class TestDog(unittest.TestCase):

    def test_age_set(self):
        dog_age = Dog(1)
        self.assertEqual(dog_age.human_age(), 7)

    def test_re_age(self):
        dog_age = Dog(2)
        self.assertEqual(dog_age.human_age(), 14)

        dog_age.age = 3
        self.assertEqual(dog_age.human_age(), 21)

        dog_age.age = 7
        self.assertEqual(dog_age.human_age(), 49)

    def test_type_return(self):
        dog_age = Dog(2)
        self.assertEqual(type(dog_age.human_age()), int)

        dog_age = Dog(13)
        self.assertEqual(type(dog_age.human_age()), int)


# start
def main():
    unittest.main()


if __name__ == '__main__':
    ...
