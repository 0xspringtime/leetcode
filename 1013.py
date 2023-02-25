def canThreePartsEqualSum(A) -> bool:
    total = sum(A)
    if total % 3 != 0: return False
    count, cumsum, target = 0, 0, total // 3
    for num in A:
        cumsum += num
        if cumsum == target:
            cumsum = 0
            count += 1
    return count >= 3
#O(m*n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [0,2,1,-6,6,-7,9,1,2,0,1],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [0,2,1,-6,6,7,9,-1,2,0,1],
            "expected": False
        },
        {
            "name": "list with one item",
            "input": [3,3,6,5,-2,2,5,1,-9,4],
            "expected": True
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == canThreePartsEqualSum(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))