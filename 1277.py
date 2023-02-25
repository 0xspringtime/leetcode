def countSquares(matrix) -> int:
    rowLen = len(matrix)
    colLen = len(matrix[0])
    memo = [[0] * colLen for _ in range(rowLen)]
    count = 0

    for row in range(rowLen):
        for col in range(colLen):
            if matrix[row][col] == 1:
                memo[row][col] = 1 + min(memo[row][col - 1], memo[row - 1][col], memo[row - 1][col - 1])
                count += memo[row][col]

    return count

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
],
            "expected": 15
        },
        {
            "name": "simple case 2",
            "input": [
  [1,0,1],
  [1,1,0],
  [1,1,0]
],
            "expected": 7
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == countSquares(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))