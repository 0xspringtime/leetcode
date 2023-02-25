from typing import List
def partition(s: str) -> List[List[str]]:
    res, part = [], []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range(i, len(s)):
            if isPali(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1)
                part.pop()

    dfs(0)
    return res

def isPali(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

def test():
    test_cases = [
        {
            "name": "example 1",
            "input": "aab",
            "expected": [["a","a","b"],["aa","b"]]
        },
        {
            "name": "example 2",
            "input": "a",
            "expected": [["a"]]
        }
    ]
    for test_case in test_cases:
        assert test_case["expected"] == partition(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
