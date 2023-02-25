from typing import List
def minSwaps(grid: List[List[int]]) -> int:
    swaps = 0
    zeroesNeeded = len(grid) - 1
    start = 1

    for i in range(len(grid)):
        temp = i
        while temp < len(grid) and grid[temp][start:] != [0] * zeroesNeeded:
            temp += 1

        if temp >= len(grid):
            return -1

        start += 1
        zeroesNeeded -= 1

        while temp > i:
            grid[temp], grid[temp - 1] = grid[temp - 1], grid[temp]
            temp -= 1
            swaps += 1

    return swaps

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input":[[0,0,1],[1,1,0],[1,0,0]],
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
            "expected": -1
        },
        {
            "name": "simple case 3",
            "input": [[1,0,0],[1,1,0],[1,1,1]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minSwaps(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))