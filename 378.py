from bisect import *
def kthSmallest(matrix, k) -> int:
    l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

    def less_k(m):
        cnt = 0  # count
        for r in range(N):
            # binary search
            x = bisect_right(matrix[r], m)
            cnt += x
        return cnt

    while l < r:
        mid = (l + r) // 2

        if less_k(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,5,9],[10,11,13],[12,13,15]],
            "input1": 8,
            "expected": 13
        },
        {
            "name": "simple case 2",
            "input": [[-5]],
            "input1": 1,
            "expected": -5
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == kthSmallest(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))