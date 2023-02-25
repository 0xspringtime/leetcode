def lengthOfLongestSubstring(s: str) -> int:
    sub = set()
    j, l, m = 0, 0, 0

    while j < len(s):
        while s[j] in sub:
            sub.remove(s[l])
            l += 1
        sub.add(s[j])
        m = max(m, j - l + 1)
        j += 1
    return m


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "abcabcbb",
            "expected": 3
        },
        {
            "name": "simple case 2",
            "input": "bbbbb",
            "expected":  1
        },
        {
            "name": "simple case 3",
            "input": "pwwkew",
            "expected":  3
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == lengthOfLongestSubstring(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))