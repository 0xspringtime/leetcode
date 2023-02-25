import collections
def groupAnagrams(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["eat","tea","tan","ate","nat","bat"],
            "expected": [["bat"],["nat","tan"],["ate","eat","tea"]]
        },
        {
            "name": "simple case 2",
            "input": [""],
            "expected": [[""]]
        },
        {
            "name": "list with one item",
            "input": ["a"],
            "expected": [["a"]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == groupAnagrams(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))