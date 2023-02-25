def minCost(startPos, homePos, rowCosts, colCosts) -> int:
    def getRange(left, right, array):
        if left > right:
            right, left = left, right
        return sum((array[i] for i in range(left, right + 1)))

    totalRowCost = getRange(startPos[0], homePos[0], rowCosts)
    totalColCost = getRange(startPos[1], homePos[1], colCosts)

    # Don't pay for the position you start out on
    return totalRowCost + totalColCost - rowCosts[startPos[0]] - colCosts[startPos[1]]

#greedy O(1) space

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 0],
            "input1": [2, 3],
            "input2": [5, 4, 3],
            "input3": [8, 2, 6, 7],
            "expected": 18
        },
        {
            "name": "simple case 1",
            "input": [0, 0],
            "input1": [0, 0],
            "input2": [5],
            "input3": [26],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minCost(test_case["input"], test_case["input1"], test_case["input2"], test_case["input3"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))