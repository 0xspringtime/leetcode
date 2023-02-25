from collections import *
def intersect(nums1, nums2):
    counts = {}
    res = []

    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    for num in nums2:
        if num in counts and counts[num] > 0:
            res.append(num)
            counts[num] -= 1

    return res

def intersect1(nums1, nums2):
    a, b = map(Counter, (nums1, nums2))
    return list((a & b).elements())

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,2,1],
            "input1": [2,2],
            "expected": [2,2]
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == intersect1(test_case["input1"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))