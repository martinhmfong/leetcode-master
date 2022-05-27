def binary_search(input_array, value):
    """Your code goes here."""
    left, right = 0, len(input_array) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = input_array[mid]
        if mid_value == value:
            return mid
        if mid_value > value:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)


if __name__ == '__main__':
    test_list = [1, 3, 9, 11, 15, 19, 29]
    print(binary_search(test_list, 15))
