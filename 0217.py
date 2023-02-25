def containsDuplicate(nums) -> bool:
    hs = set()

    for n in nums:
        if n in hs:
            return True
        hs.add(n)
    return False

def containsDuplicate1(nums):
    return len(nums) != len(set(nums))

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,3,1],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [1,2,3,4],
            "expected": False
        },
        {
            "name": "list with one item",
            "input": [1,1,1,3,3,4,3,2,4,2],
            "expected": True
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == containsDuplicate1(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
