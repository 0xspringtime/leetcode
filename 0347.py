def topKFrequent(nums, k: int):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
#O(N)
from collections import *
def topKFrequent1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Use Counter to extract the top k frequent elements
    # most_common(k) return a list of tuples, where the first item of the tuple is the element,
    # and the second item of the tuple is the count
    # Thus, the built-in zip function could be used to extract the first item from the tuples
    return map(list, zip(*Counter(nums).most_common(k))[0])

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,1,1,2,2,3],
            "input1": 2,
            "expected": [1,2]
        },
        {
            "name": "simple case 2",
            "input": [1],
            "input1": 1,
            "expected": [1]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == topKFrequent(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))