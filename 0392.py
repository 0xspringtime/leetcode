def isSubsequence(s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)



def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "abc",
            "input1": "ahbgdc",
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": "axc",
            "input1": "ahbgdc",
            "expected": False 
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isSubsequence(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
