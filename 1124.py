def longestWPI(hours):
    res = score = 0
    seen = {}
    for i, h in enumerate(hours):
        score = score + 1 if h > 8 else score - 1
        if score > 0:
            res = i + 1
        seen.setdefault(score, i)
        if score - 1 in seen:
            res = max(res, i - seen[score - 1])
    return res
#O(n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [9,9,6,0,6,6,9],
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": [6,6,6],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == longestWPI(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))