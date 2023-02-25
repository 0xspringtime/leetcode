def spiralOrder(matrix):
        return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "expected": [1,2,3,6,9,8,7,4,5]
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
            "expected": [1,2,3,4,8,12,11,10,9,5,6,7]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == spiralOrder(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))