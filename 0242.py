def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT

from collections import *
def isAnagram1(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "anagram",
            "input1": "nagaram",
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": "rat",
            "input1": "car",
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isAnagram(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
