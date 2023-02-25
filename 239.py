from collections import *
def maxSlidingWindow(nums, k):
    output = []
    q = deque()  # index
    l = r = 0
    # O(n) O(n)
    while r < len(nums):
        # pop smaller values from q
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left val from window
        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1

    return output

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,3,-1,-3,5,3,6,7],
            "input1": 3,
            "expected": [3,3,5,5,6,7]
        },
        {
            "name": "simple case 2",
            "input": [1],
            "input1": 1,
            "expected": [1]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxSlidingWindow(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))