from typing import List
def permute(nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "expected": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        },
        {
            "name": "simple case 2",
            "input": [0, 1],
            "expected": [[0,1],[1,0]]
        },
        {
            "name": "list with one item",
            "input": [1],
            "expected": [[1]] 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == permute(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
