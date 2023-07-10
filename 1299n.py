from typing import List

def replaceElements(arr: List[int]) -> List[int]:
    # Start with -1 for the greatest element in the rightmost side
    greatest_element = -1

    # Start from the end of the list
    for i in range(len(arr) - 1, -1, -1):
        # The new greatest element is the max between the current element and the last greatest element
        new_greatest_element = max(greatest_element, arr[i])
        
        # Replace the current element with the greatest element
        arr[i] = greatest_element
        
        # Update the greatest element
        greatest_element = new_greatest_element

    return arr
#time O(n)
#space O(1)
