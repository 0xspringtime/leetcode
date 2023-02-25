from typing import List
def luckyNumbers(matrix):
    minrow = {min(r) for r in matrix}
    maxcol = {max(c) for c in zip(*matrix)}
    return list(minrow & maxcol)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[3, 7, 8], [9, 11, 13], [15, 16, 17]],
            "expected": [15]
        },
        {
            "name": "simple case 2",
            "input": [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]],
            "expected": [12]
        },
        {
            "name": "simple case 3",
            "input": [[7,8],[1,2]],
            "expected": [7]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == luckyNumbers(test_case["input"]), test_case["name"]

print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
from datetime import datetime

start_time = datetime.now()
test()
print("Everything passed")
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
