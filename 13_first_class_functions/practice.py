# def my_sqrt(x):
#     return x ** 2
#
#
# def my_double(x):
#     return x * 2
#
#
# def my_reduce_by_2(x):
#     return x / 2
#
#
# def my_func(func, x):
#     print(func(x))
#
#
# print(my_func(my_double, 15))
#
#
# func_dict = {1: my_double,
#              2: my_reduce_by_2,
#              3: my_sqrt
#              }
#
# try:
#     print(func_dict.get(3)(6))
#
# except TypeError:
#     print('ur clown')


# def double(x):
#     return x * 2
#
#
# def do_triple(f):
#     def result_func(x):
#         return f(f(f(x)))
#     return result_func
#
#
# res = do_triple(double)
# print(res(2))


# def is_type(num):
#     if not isinstance(num, int):
#         raise TypeError('must be int')
#
#
# def is_positive(num):
#     if num < 0:
#         raise ValueError('wtf')
#
#
# def recursive(num):
#     is_type(num)
#     is_positive(num)
#     if num <= 1:
#         return 1
#
#     return num * recursive(num - 1)
#
#
# print(recursive(5))list(filtered_txt
#
#
# """ This is docstring for this script."""
user_txt = 'Leva'
txt = f"{user_txt}drinks pepsi in his brand new BMW!"
