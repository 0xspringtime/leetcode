def carFleet(target: int, position, speed) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 12,
            "input1": [10,8,0,5,3],
            "input2": [2,4,1,1,3],
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": 10,
            "input1": [3],
            "input2": [3],
            "expected": 1
        },
        {
            "name": "simple case 3",
            "input": 100,
            "input1": [0,2,4],
            "input2": [4,2,1],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == carFleet(test_case["input"], test_case["input1"], test_case["input2"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))