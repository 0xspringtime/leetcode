def generateMatrix(n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [[*range(lo, hi)]] + [list(j) for j in zip(*A[::-1])]
        return A

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 3,
            "expected": [[1,2,3],[8,9,4],[7,6,5]]
        },
        {
            "name": "simple case 2",
            "input": 1,
            "expected": [[1]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == generateMatrix(test_case["input"]), test_case["name"]

from datetime import datetime
start_time = datetime.now()
test()
print("Everything passed")
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))