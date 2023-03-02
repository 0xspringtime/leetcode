from typing import List 
def plusOne(digits: List[int]) -> List[int]:
    one = 1
    i = 0
    digits = digits[::-1]

    while one:
        if i < len(digits):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                one = 0
        else:
            digits.append(one)
            one = 0
        i += 1
    return digits[::-1]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "expected": [1,2,4]
        },
        {
            "name": "simple case 2",
            "input": [4,3,2,1],
            "expected": [4,3,2,2] 
        },
        {
            "name": "list with one item",
            "input": [9],
            "expected": [1,0]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == plusOne(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
