def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [73,74,75,71,69,72,76,73],
            "expected": [1,1,4,2,1,1,0,0]
        },
        {
            "name": "simple case 2",
            "input": [30,40,50,60],
            "expected": [1,1,1,0]
        },
        {
            "name": "simple case 2",
            "input": [30,60,90],
            "expected": [1,1,0]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == dailyTemperatures(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))