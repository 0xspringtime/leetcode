def minOperations(grid, x) -> int:
    n = len(grid) * len(grid[0])
    ops = 0
    med = sorted([col for row in grid for col in row])[n // 2]
    for row in grid:


        for col in row:
            # If the difference is not divisible, you can't add/subtract your way to the median
            if abs(med - col) % x != 0:
                return -1
            ops += abs(med - col) // x

# Profit
    return ops


# Find the median
#   Convert grid to a 1D list
#   Index the middle element (when it's even, it picks the second middle)


# Go through the grid and calculate the number of additions/subtractions needed for each element
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[2,4],[6,8]],
            "input1": 2,
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [[1,5],[2,3]],
            "input1": 1,
            "expected": 5
        },
        {
            "name": "list with one item",
            "input": [[1,2],[3,4]],
            "input1": 2,
            "expected": -1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minOperations(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))