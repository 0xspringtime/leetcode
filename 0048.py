def rotate(A):
    A[:] = map(list, zip(*A[::-1]))
    return A


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "expected": [[7,4,1],[8,5,2],[9,6,3]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == rotate(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))