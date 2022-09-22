# imports
from random import randint


# task 1
# O(n^2)
def bubble_sort(array: list[int]) -> None:

    for i in range(len(array) - 1, 0, -1):

        for j in range(len(array) - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


# task 2
# 0(n)
def merge(left: list[int], right: list[int]) -> list[int]:
    i = 0
    j = 0
    merged = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1

        else:
            merged.append(right[j])
            j += 1

    merged += left[i:] + right[j:]

    return merged


# 0(n log n)
def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    return merge(
        left=merge_sort(array[:mid]),
        right=merge_sort(array[mid:])
    )


# task 3
# O(n log n)
def quick_sort(array):
    if len(array) > 1:
        pivot = array[randint(0, len(array) - 1)]

        low_values = [value for value in array if value < pivot]

        equal_values = [value for value in array if value == pivot]

        high_values = [value for value in array if value > pivot]

        array = quick_sort(low_values) + equal_values + quick_sort(high_values)

    return array


# start
def main():
    # task 1
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    bubble_sort(items)
    bubble_sort(lst)
    print("bubble_sort: (items)", items)
    print("bubble_sort: (random)", lst)
    # task 1
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    print("merge_sort: (items)", merge_sort(items))
    print("merge_sort: (random)", merge_sort(lst))
    # task 3
    items = [2, 4, 1, 3, 5, 7, 6, 9, 8, 0]
    lst = [randint(1, 100) for _ in range(20)]
    print("quick sort: (items)", quick_sort(items))
    print("quick sort: (random)", quick_sort(lst))


if __name__ == '__main__':
    main()