from typing import List
def jump(nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,3,1,1,4],
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": [2,3,0,1,4],
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == jump(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
