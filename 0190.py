def reverse(n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 0b00000010100101000001111010011100,
            "expected": 964176192
        },
        {
            "name": "simple case 2",
            "input": 0b11111111111111111111111111111101,
            "expected": 3221225471
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == reverse(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
