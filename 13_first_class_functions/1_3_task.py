#   task 1
def some_variable():
    a = 'hello world'
    z_list = [1, 4, 9]
    x = True
    return a + str(z_list) + str(x)


def local_variables_in_func(func):
    return func.__code__.co_nlocals
# task 2


def text_upper(text):
    return text.upper()


def text_lower(text):
    return text.lower()


def text_title(text):
    return text.title()


func_dict = {1: text_upper,
             2: text_lower,
             3: text_title
             }
user_text = 'sEe you Later. dude!'

# def text_redactor(func, text):
#     return func(text)

# print(text_redactor(text_title, user_text))

# task 3

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums, func1, func2):
    for num in nums:
        if num < 1:
            return func2(nums)
    return func1(nums)
###############################################################################


def main():
    print(local_variables_in_func(some_variable))
    print(func_dict[1](user_text))
    print(choose_func(nums1, square_nums, remove_negatives))


if __name__ == '__main__':
    main()
