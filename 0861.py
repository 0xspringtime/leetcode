def matrixScore(A):
    M, N = len(A), len(A[0])
    res = (1 << N - 1) * M
    for j in range(1, N):
        cur = sum(A[i][j] == A[i][0] for i in range(M))
        res += max(cur, M - cur) * (1 << N - 1 - j)
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,0,1,1],[1,0,1,0],[1,1,0,0]],
            "expected": 39
        },
        {
            "name": "simple case 2",
            "input": [[0]],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == matrixScore(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))