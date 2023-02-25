def reconstructMatrix(upper: int, lower: int, colsum):
    s, n = sum(colsum), len(colsum)
    if upper + lower != s: return []
    u, d = [0] * n, [0] * n
    for i in range(n):
        if colsum[i] == 2 and upper > 0 and lower > 0:
            u[i] = d[i] = 1
            upper, lower = upper - 1, lower - 1
        elif colsum[i] == 1:
            if upper > 0 and upper >= lower:
                u[i], upper = 1, upper - 1
            elif lower > 0 and lower > upper:
                d[i], lower = 1, lower - 1
            else:
                return []
        elif not colsum[i]:
            continue
        else:
            return []
    return [u, d]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 2,
            "input1": 1,
            "input2":  [1,1,1],
            "expected": [[1,1,0],[0,0,1]]
        },
        {
            "name": "simple case 2",
            "input": 2,
            "input1": 3,
            "input2": [2,2,1,1],
            "expected": []
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == reconstructMatrix(test_case["input"], test_case["input1"], test_case["input2"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))