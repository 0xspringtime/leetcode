from typing import List
def countNegatives(grid: List[List[int]]) -> int:
    return sum(a < 0 for i in grid for a in i)
#O(n^2)

def countNegatives1(grid):
     i = len(grid) - 1
     j = 0
     count = 0
     while i >= 0 and j < len(grid[0]):
         print(i, j)
         if grid[i][j] < 0:
             count += len(grid[0]) - j
             i -= 1
         else:
             j += 1
     return (count)
#O(m+n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]],
            "expected": 8
        },
        {
            "name": "simple case 2",
            "input": [[3,2],[1,0]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == countNegatives1(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
