from collections import defaultdict
def findDiagonalOrder(mat):
    R, C = len(mat), len(mat[0])
    diagonalDict = defaultdict(list)
    # key - diagonal elements have the same r + c value.
    for r in range(R):
        for c in range(C):
            diagonalDict[r + c].append(mat[r][c])
    ans = []
    for i, value in enumerate(diagonalDict.values()):
        if i % 2 == 0:
            ans += value[::-1]
        else:
            ans += value
    return ans

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "expected":[1,2,4,7,5,3,6,8,9]
        },
        {
            "name": "simple case 2",
            "input": [[1,2],[3,4]],
            "expected": [1,2,3,4]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findDiagonalOrder(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))