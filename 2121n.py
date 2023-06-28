def sumOfIntervals(arr):
    # Initialize an empty dictionary to store the indices
    indices = {}

    # Initialize the result list with zeros
    result = [0] * len(arr)

    for i, val in enumerate(arr):
        # If the value already exists in the dictionary
        if val in indices:
            # For each index where the same value was found before
            for index in indices[val]:
                # Calculate the interval and add it to the sum of intervals for the current index and for the index where the same value was found before
                interval = i - index
                result[i] += interval
                result[index] += interval
            # Add the current index to the list of indices for the current value
            indices[val].append(i)
        else:
            # If the value doesn't exist in the dictionary, add a new entry with the current index
            indices[val] = [i]

    return result
#time O(n^2)
#space O(n)
