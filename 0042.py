def trap(height) -> int:
    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [0,1,0,2,1,0,1,3,2,1,2,1],
            "expected": 6
        },
        {
            "name": "simple case 2",
            "input": [4,2,0,3,2,5],
            "expected": 9
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == trap(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))