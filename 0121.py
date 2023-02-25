from typing import List
def maxProfit(prices: List[int]) -> int:
    res = 0

    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [7,1,5,3,6,4],
            "expected": 5
        },
        {
            "name": "simple case 2",
            "input": [7,6,4,3,1],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxProfit(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
