def freqAlphabets(s: str) -> str:
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s

def test():
    test_cases = [
        {
            "name": "example 1",
            "input": "10#11#12",
            "expected": "jkab"
        },
        {
            "name": "example 2",
            "input": "1326#",
            "expected": "acz"
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == freqAlphabets(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
