def findPeakGrid(mat):
    top = 0
    bottom = len(mat) - 1
    while bottom > top:
        mid = (top + bottom) // 2
        if max(mat[mid]) > max(mat[mid + 1]):
            bottom = mid
        else:
            top = mid + 1
    return [bottom, mat[bottom].index(max(mat[bottom]))]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,4],[3,2]],
            "expected": [0,1]
        },
        {
            "name": "simple case 2",
            "input": [[10,20,15],[21,30,14],[7,16,32]],
            "expected": [2,2]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findPeakGrid(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))