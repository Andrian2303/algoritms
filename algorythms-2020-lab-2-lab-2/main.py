import doctest


def merge_sort(array):
    """
    Sorts the corresponding array by merge sorting
    >>> merge_sort([-7, 54, 66, -1, 20, 3, 1])
    [-7, -1, 1, 3, 20, 54, 66]
    >>> merge_sort([6, 8, 1, 14, 3, 9, 2])
    [1, 2, 3, 6, 8, 9, 14]
    >>> merge_sort([-56, -2, -63, -25, -47, -6])
    [-63, -56, -47, -25, -6, -2]
    """
    if len(array) > 1:
        middle_pos = len(array) // 2
        left = array[:middle_pos]
        right = array[middle_pos:]

        left = merge_sort(left)
        right = merge_sort(right)

        left_pos = right_pos = original_pos = 0

        while left_pos < len(left) and right_pos < len(right):
            if left[left_pos] < right[right_pos]:
                array[original_pos] = left[left_pos]
                left_pos += 1
            else:
                array[original_pos] = right[right_pos]
                right_pos += 1
            original_pos += 1

        while left_pos < len(left):
            array[original_pos] = left[left_pos]
            left_pos += 1
            original_pos += 1

        while right_pos < len(right):
            array[original_pos] = right[right_pos]

            right_pos += 1
            original_pos += 1

    return array


def correct_value_of_bananas_per_hour(bananas_per_hour, piles, eating_hours, current_index):
    """
    Returns true if bananas in piles can be eaten in eating_hours
    >>> correct_value_of_bananas_per_hour(6, [2, 6, 10], 6, 1)
    True
    >>> correct_value_of_bananas_per_hour(4, [10, 10, 10], 5, 0)
    False
    >>> correct_value_of_bananas_per_hour(18, [5, 7, 16, 18, 34], 5, 3)
    False
    >>> correct_value_of_bananas_per_hour(29, [4, 13, 19, 29, 30], 6, 3)
    True
    """
    total_hours = current_index
    for pile in piles[current_index:]:
        total_hours += (pile // bananas_per_hour) + (1 if (pile % bananas_per_hour) > 0 else 0)
    return total_hours <= eating_hours


def binary_search(min, max, piles, eating_hours, index):
    """
    Search min number in range from min value to max value
    that fits condition of correct_value_of_bananas_per_hour
    >>> binary_search(23, 30, [4 ,11 ,20 ,23, 30], 5, 3)
    30
    """
    if abs(max - min) == 1:
        return max

    middle = (min + max) // 2
    if correct_value_of_bananas_per_hour(middle, piles, eating_hours, index):
        return binary_search(min, middle, piles, eating_hours, index)
    else:
        return binary_search(max, middle, piles, eating_hours, index)


def count_bananas_per_hour(piles, eating_hours):
    """
    Returns counted quantity on bananas per hour
    >>> count_bananas_per_hour([3, 6, 7, 11], 8)
    4
    >>> count_bananas_per_hour([30, 11, 23, 4, 20], 5)
    30
    >>> count_bananas_per_hour([30, 11, 23, 4, 20], 6)
    23
    >>> count_bananas_per_hour([30, 11, 14, 4, 13], 6)
    15
    >>> count_bananas_per_hour([4, 4], 6)
    2
    """
    sorted_piles = merge_sort(piles)

    if len(sorted_piles) == eating_hours:
        return sorted_piles[-1]

    bigger_value = sorted_piles[-1]
    last_index = 0
    for index in range(len(sorted_piles) - 2, -1):
        bananas_per_hour = sorted_piles[index]
        smaller_value = bananas_per_hour
        if not correct_value_of_bananas_per_hour(bananas_per_hour, sorted_piles, eating_hours, index):
            last_index = index
            break
        bigger_value = bananas_per_hour
    else:
        smaller_value = 0

    return binary_search(smaller_value, bigger_value, sorted_piles, eating_hours, last_index)


if __name__ == '__main__':
    doctest.testmod(verbose=True)

    piles = [30, 11, 23, 4, 20]
    hours = 6
    bananas_per_hour = count_bananas_per_hour(piles, hours)
    print(bananas_per_hour)
