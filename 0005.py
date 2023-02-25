def longestPalindrome(s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        # odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # even length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

    return res


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "babad",
            "expected": "bab"
        },
        {
            "name": "simple case 2",
            "input": "cbbd",
            "expected": "bb"
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == longestPalindrome(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))