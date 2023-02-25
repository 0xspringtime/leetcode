from typing import List
def maximumWealth(accounts: List[List[int]]) -> int:
    return max(sum(acc) for acc in accounts)
#O(m*n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[3,2,1]],
            "expected": 6
        },
        {
            "name": "simple case 2",
            "input": [[1,5],[7,3],[3,5]],
            "expected": 10
        },
        {
            "name": "list with one item",
            "input": [[2,8,7],[7,1,3],[1,9,5]],
            "expected": 17
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maximumWealth(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))