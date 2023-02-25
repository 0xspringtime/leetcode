def findRotation(mat, target) -> bool:
    def rc(A):
        A[:] = map(list, zip(*A[::-1]))
        return A

    return True if mat == target or rc(mat) == target or rc(rc(mat)) == target or rc(rc(rc(mat))) == target else False

def findRotation1(mat, target) -> bool:
    k = 0
    while k < 4:
        for i in range(len(mat)):
            for j in range(i, len(mat)):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        k += 1

        for i in range(len(mat)):
            mat[i].reverse()
        print(mat)
        if mat == target:
            return True
        else:
            continue
    return False

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,1],[1,0]],
            "input1": [[1,0],[0,1]],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [[0,1],[1,1]],
            "input1": [[1,0],[0,1]],
            "expected": False
        },
        {
            "name": "simple case 3",
            "input": [[0,0,0],[0,1,0],[1,1,1]],
            "input1": [[1,1,1],[0,1,0],[0,0,0]],
            "expected": True
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findRotation(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))