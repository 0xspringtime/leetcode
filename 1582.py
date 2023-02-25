def numSpecial(mat) -> int:
    res = 0
    rows = len(mat)
    cols = len(mat[0])

    rowtotals = []
    coltotals = []

    # Store the sum of each row
    for row in mat:
        rowtotals.append(sum(row))

    # Store the sum of each column
    for col in zip(*mat):
        coltotals.append(sum(col))

    # Check if current position is "1" and is the only "1" in that row and column
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1 and rowtotals[i] == 1 and coltotals[j] == 1:
                res += 1

    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,0,0],[0,0,1],[1,0,0]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[1,0,0],[0,1,0],[0,0,1]],
            "expected": 3
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == numSpecial(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))