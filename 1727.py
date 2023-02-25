def largestSubmatrix(matrix) -> int:
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0 and row > 0:
                matrix[row][col] += matrix[row - 1][col]

        curr = sorted(matrix[row], reverse=True)
        for i in range(len(matrix[0])):
            ans = max(ans, curr[i] * (i + 1))

    return ans

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,0,1],[1,1,1],[1,0,1]],
            "expected": 4
        },
        {
            "name": "simple case 2",
            "input": [[1,0,1,0,1]],
            "expected": 3
        },
        {
            "name": "list with one item",
            "input": [[1,1,0],[1,0,1]],
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == largestSubmatrix(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))