def average(s):
    dic, str = {}, "x" + s[:9]
    for i in range(9, len(s)):
        str = str[1:] + s[i]
        dic[str] = 1 if str not in dic else dic[str] + 1
    return [k for k, v in dic.items() if v > 1]


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
            "expected": ["AAAAACCCCC","CCCCCAAAAA"] 
        },
        {
            "name": "simple case 2",
            "input": "AAAAAAAAAAAAA",
            "expected":["AAAAAAAAAA"] 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
