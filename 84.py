def largestRectangleArea(heights) -> int:
    maxArea = 0
    stack = []  # pair: (index, height)

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,1,5,6,2,3],
            "expected": 10
        },
        {
            "name": "simple case 2",
            "input": [2,4],
            "expected": 4
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == largestRectangleArea(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))