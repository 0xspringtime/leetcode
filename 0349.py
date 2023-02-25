def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
#O(m+n)

def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    map = {}
    for i in nums1:
        map[i] = map[i] + 1 if i in map else 1
    for j in nums2:
        if j in map and map[j] > 0:
            res.append(j)
            map[j] = 0

    return res
#O(m+n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,2,1],
            "input1": [2,2],
            "expected": [2]
        },
        {
            "name": "simple case 2",
            "input": [4,9,5],
            "input1": [9,4,9,8,4],
            "expected": [9,4]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == intersection(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))