from typing import List
def shiftGrid(grid,  k):
    M, N = len(grid), len(grid[0])

    def posToVal(r, c):
        return r * N + c
    def valToPos(v):
        return [v // N, v % N]

    res = [[0] * N for i in range(M)]
    for r in range(M):
            for c in range(N):
                newVal = (posToVal(r,c) + k) % (M*N)
                newR, newC = valToPos(newVal)
                res[newR][newC] = grid[r][c]
    return res
#O(m*n)
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "input1": 1,
            "expected": [[9,1,2],[3,4,5],[6,7,8]]
        },
        {
            "name": "simple case 2",
            "input": [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]],
            "input1": 4,
            "expected": [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        },
        {
            "name": "list with one item",
            "input": [[1,2,3],[4,5,6],[7,8,9]],
            "input1": 9,
            "expected": [[1,2,3],[4,5,6],[7,8,9]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == shiftGrid(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))