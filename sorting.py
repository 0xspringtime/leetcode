def sort_tuples(tuples):
    # Sort tuples based on second element
    tuples.sort(key=lambda x: x[1])
    return tuples

tuples = [(1, 5), (2, 3), (4, 2), (3, 1)]
print(sort_tuples(tuples))  # Output: [(3, 1), (4, 2), (2, 3), (1, 5)]

