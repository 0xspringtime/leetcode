def checkValid(matrix) -> bool:
    get = set(range(1, len(matrix) + 1))
    return all(get == set(x) for x in matrix + list(zip(*matrix)))

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input":[[1,2,3],[3,1,2],[2,3,1]],
            "expected":True
        },
        {
            "name": "simple case 2",
            "input": [[1,1,1],[1,2,3],[1,2,3]],
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == checkValid(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))