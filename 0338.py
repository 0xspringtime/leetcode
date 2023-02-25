from typing import List
def countBits(n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input":  2,
            "expected": [0,1,1] 
        },
        {
            "name": "simple case 2",
            "input": 5,
            "expected": [0,1,1,2,1,2]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == countBits(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
