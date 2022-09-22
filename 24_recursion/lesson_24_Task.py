# imports
from typing import Union


# task 1
def to_power(x: Union[int, float], exp: int, result=0) -> Union[int, float]:
    if exp < 0:
        raise ValueError('This function work only with exp > 0.')
    if x == 0:
        return result
    result = to_power(x - x, exp, result + (x ** exp))
    return result


# task 2
def is_palindrome(_str: str, index: int = 0) -> bool:
    _str = _str.lower()
    index = len(_str)

    if index < 2:
        return True
    elif _str[0] == _str[index - 1]:
        return is_palindrome(_str[1:index - 1])
    else:
        return False


# task 3
def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        raise ValueError('This function works only with positive integers')
    if n == 0:
        return n
    return a + mult(a, n - 1)


# task 4
def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]


# task 5
def sum_of_digits(_str: str) -> int:
    sum_ = 0
    for i in _str:
        if i.isdigit():
            sum_ += int(i)
        else:
            raise ValueError('input string must be digit string')
    return sum_


# start
def main():
    # task 1
    print(to_power(2, 3))
    print(to_power(3.5, 2))
    # task 2
    print(is_palindrome('mom'))
    print(is_palindrome('sassas'))
    print(is_palindrome('o'))
    # task 3
    print(mult(2, 4))
    print(mult(2, 0))
    # task 4
    print(reverse('hello'))
    print(reverse('o'))
    # task 5
    print(sum_of_digits('26') == 8)


if __name__ == '__main__':
    main()