def isHappy(n: int) -> bool:
    slow, fast = n, sumSquareDigits(n)

    while slow != fast:
        fast = sumSquareDigits(fast)
        fast = sumSquareDigits(fast)
        slow = sumSquareDigits(slow)

    return True if fast == 1 else False

def sumSquareDigits(n):
    output = 0
    while n:
        output += (n % 10) ** 2
        n = n // 10
    return output

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 19,
            "expected": True 
        },
        {
            "name": "simple case 2",
            "input": 2,
            "expected": False 
        }
	]

    for test_case in test_cases:
        assert test_case["expected"] == isHappy(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
