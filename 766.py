def isToeplitzMatrix(matrix) -> bool:
    for i in range(1, len(matrix)):
        for j in range(1, len(list(zip(*matrix)))):
            if matrix[i - 1][j - 1] != matrix[i][j]:
                return False
    return True

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3,4],[5,1,2,3],[9,5,1,2]],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[1,2],[2,2]],
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isToeplitzMatrix(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))