def maximalSquare(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] = int(A[i][j])
            if A[i][j] and i and j:
                A[i][j] = min(A[i - 1][j], A[i - 1][j - 1], A[i][j - 1]) + 1
    return len(A) and max(map(max, A)) ** 2

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [["0","1"],["1","0"]],
            "expected": 1
        },
        {
            "name": "list with one item",
            "input": [["0"]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maximalSquare(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))