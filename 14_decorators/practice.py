# from functools import wraps
#
# result = {}
#
#
# def test(function):
#     @wraps(function)
#     def wrap(*args, **kwargs):
#         function_result = function(*args, **kwargs)
#         if args not in result:
#             result[args] = function_result
#         else:
#             return result.get(args)
#         return result
#     return wrap
#
#
# @test
# def add(x, y):
#     return x + y
#
#
# def main():
#     print(add(5, 3))
#     print(add(5, 7))
#     print(add(2, 1))
#     print(add(2, 1))
#     print(add(2, 6))
#
#
# if __name__ == "__main__":
#     main()

