def isPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphanum(s[l]):
            l += 1
        while l < r and not alphanum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def isPalindrome1(s: str) -> bool:
    s = [i for i in s.lower() if i.isalnum()]
    return s == s[::-1]

# Could write own alpha-numeric function
def alphanum(c):
    return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
    )
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "A man, a plan, a canal: Panama",
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": "race a car",
            "expected": False
        },
        {
            "name": "list with one item",
            "input": " ",
            "expected": True
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isPalindrome(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))