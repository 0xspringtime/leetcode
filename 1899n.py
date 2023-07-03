#greedy
def mergeTriplets(triplets, target):
    # Step 1: Initialize the current maximum triplet as [0, 0, 0].
    current_max = [0, 0, 0]
    # Step 2: Sort the triplets in descending order of the sum of their elements.
    triplets.sort(key=sum, reverse=True)

    # Step 3: Iterate over the sorted triplets.
    for triplet in triplets:
        # Check if the triplet's elements are all less than or equal to their corresponding target triplet's elements,
        # and at least one element is greater than the current maximum.
        if all(a <= b for a, b in zip(triplet, target)) and any(a > b for a, b in zip(triplet, current_max)):
            # Update the current maximum.
            current_max = [max(a, b) for a, b in zip(current_max, triplet)]

    # Step 4: Check if the current maximum triplet is equal to the target triplet.
    return current_max == target
#time O(nlogn)
#space O(1)
