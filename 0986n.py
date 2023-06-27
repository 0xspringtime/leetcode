#two pointer
def intervalIntersection(firstList, secondList):
    i, j = 0, 0  # Initialize pointers for both lists
    result = []  # Initialize result list

    # While there are still intervals to check in both lists
    while i < len(firstList) and j < len(secondList):
        # Get the max start and min end of the two intervals
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        # If the start is less than or equal to the end, there is an intersection
        if start <= end:
            result.append([start, end])

        # Increment the pointer for the list with the interval that ends first
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result
#time O(n+m)
#space O(n+m)
