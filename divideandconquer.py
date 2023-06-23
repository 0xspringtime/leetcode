def mergeSort(arr):
    # If the array has only one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquer by recursively sorting the two halves
    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    # Combine the sorted halves into a sorted whole
    return merge(left_half, right_half)


def merge(left, right):
    # Merge two sorted lists into a single sorted list
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If we have any elements left in either list, append them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    # Return the result
    return merged

#example is merge sort

#solves a problem by breaking it into smaller subproblems, solving the subproblems independently, and then combining their solutions to create a solution to the original problem

#Divide: If the list is of length 0 or 1, then it is already sorted. Otherwise, divide the unsorted list into two sublists of about half the size.
#
#Conquer: Recursively sort both sublists.
#
#Combine: Merge the two sorted sublists back into one sorted list.



