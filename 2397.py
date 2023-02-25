from typing import List
import itertools
def maximumRows(mat: List[List[int]], cols: int) -> int:
    m, n, ans = len(mat), len(mat[0]), -1

    for comb in itertools.combinations((num for num in range(n)), n - cols):
        ct = len(set(r for r in range(m) for c in comb if mat[r][c] == 1))

        ans = max(ans, m - ct)

    return ans
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,0,0],[1,0,1],[0,1,1],[0,0,1]],
            "input1": 2,
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": [[1],[0]],
            "input1": 1,
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maximumRows(test_case["input"],test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))