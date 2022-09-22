# import sys
#
# if not sys.platform.startswith('win32'):
#
#     raise Exception('Wrong system')
#
# print('Hi!')

# while True:
#     x = input('num: ')
#     try:
#         result = 10 / int(x)
#     except (ZeroDivisionError, ValueError):
#         print('ZeroDivisionError or ValueError! pls re-input your number')
#         continue
#     print(result)
#     break

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))

except ValueError:
    print("Could not convert data to an integer.")

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
