from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    m = len(mat)
    rows = sorted(range(m), key=lambda i: (mat[i], i))
    del rows[k:]
    return rows

def kWeakestRows1(G: List[List[int]], k: int) -> List[int]:
    S = [[sum(g), i] for i, g in enumerate(G)]
    R = sorted(S)
    return [r[1] for r in R[:k]]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]],
            "input1": 3,
            "expected": [2, 0, 3]
        },
        {
            "name": "simple case 2",
            "input": [[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]],
            "input1": 2,
            "expected": [0, 2]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == kWeakestRows1(test_case["input"], test_case["input1"]), test_case["name"]


if __name__ == "__main__":
    from datetime import datetime

    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
