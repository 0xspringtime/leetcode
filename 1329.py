import collections
def diagonalSort(A):
    diags = collections.defaultdict(list)
    for i, row in enumerate(A):
        for j, a in enumerate(row):
            diags[i - j].append(a)
    for diag in diags.values():
        diag.sort(reverse=True)
    for i, row in enumerate(A):
        for j, _ in enumerate(row):
            A[i][j] = diags[i - j].pop()
    return A

def diagonalSort1(mat):
    m, n = len(mat), len(mat[0])
    d = collections.defaultdict(list)
    for i in range(m):
        for j in range(n):
            d[i - j].append(mat[i][j])
    for k in d:
        d[k].sort(reverse=True)
    for i in range(m):
        for j in range(n):
            mat[i][j] = d[i - j].pop()
    return mat

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[3,3,1,1],[2,2,1,2],[1,1,1,2]],
            "expected": [[1,1,1,1],[1,2,2,2],[1,2,3,3]] 
        },
        {
            "name": "simple case 2",
            "input": [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]],
            "expected": [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]] 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == diagonalSort(test_case["input"]), test_case["name"]

test()
print("Everything passed")

