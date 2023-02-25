from typing import List
def sumZero(n: int) -> List[int]:
    return list(range(1 - n, n, 2))

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 5,
            "expected":[-4, -2, 0, 2, 4]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == sumZero(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(sumZero(5))
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
