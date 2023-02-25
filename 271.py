def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

def decode(s):
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return res
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["lint","code","love","you"],
            "expected": ["lint","code","love","you"]
        },
        {
            "name": "simple case 2",
            "input": ["we", "say", ":", "yes"],
            "expected": ["we", "say", ":", "yes"]
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