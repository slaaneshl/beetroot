import multiprocessing
import os

from dataclasses import dataclass
from time import time, sleep
from pprint import pprint
from concurrent.futures import ProcessPoolExecutor

lock = multiprocessing.Lock()
queue = multiprocessing.Queue()


def fibonacci(number):
    if number == 0:
        return 0
    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


@dataclass(frozen=True)
class Student:
    name: str
    age: int
    level: str


students = [
    Student('Oleg', 31, 'Junior'),
    Student('Vlad', 16, 'Trainee'),
    Student('Yurii', 36, 'Junior'),
    Student('Tetiana', 24, 'Junior'),
    Student('Olga', 27, 'Junior'),
    Student('Serhii', 25, 'Junior'),
    Student('Vlad', 44, 'Junior'),
    Student('Vadim', 24, 'Junior'),
    Student('Dmytro', 31, 'Junior'),
    Student('Mykola', 22, 'Junior'),
    Student('Lev', 24, 'Junior'),
    Student('Dima', 25, 'Junior'),
]


def transform(student: Student):
    print(f'Processing record {student.name}, process_id:{os.getpid()}')
    fib = fibonacci(40)
    result = {'name': student.name,
              'year_born': 2022 - student.age}

    print(f'Finished processing record {student.name}', f'fibonacci {fib}',
          f' process_id:{os.getpid()}')
    return result


if __name__ == '__main__':
    t1 = time()
    # pool = multiprocessing.Pool()
    # result = pool.map(transform, students)
    with ProcessPoolExecutor() as executor:
        for student in students:
            result = executor.submit(transform, student)
            print(result)
    print(f'Time spent to transform {time() - t1:.2f}')