def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l: r + 1] if resLen != float("infinity") else ""

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "ADOBECODEBANC",
            "input1": "ABC",
            "expected": "BANC"
        },
        {
            "name": "simple case 2",
            "input": "a",
            "input1": "a",
            "expected": "a"
        },
        {
            "name": "simple case 3",
            "input": "a",
            "input1": "aa",
            "expected": ""
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minWindow(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))