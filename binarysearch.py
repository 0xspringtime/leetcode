def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # If the element is not in the array

#Binary search is an efficient algorithm used to find a specific value (target) in a sorted collection of values (like an array or list). The algorithm works by repeatedly dividing the search interval in half. If the target value matches the middle element of the interval, the search ends. If the target value is less or greater than the middle element, the search continues on the lower or upper half of the interval, respectively.


