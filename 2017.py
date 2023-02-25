def gridGame(grid):
        
        top, bottom = grid
        top_sum = sum(top)
        bottom_sum = 0
        res = float('inf')
        
        for i in range(len(top)):
            top_sum -= top[i]
            res = min(res, max(top_sum, bottom_sum))
            bottom_sum += bottom[i]
            
        return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[2,5,4],[1,5,1]],
            "expected": 4 
        },
        {
            "name": "simple case 2",
            "input": [[3,3,1],[8,5,2]],
            "expected": 4 
        },
        {
            "name": "case 3",
            "input": [[1,3,1,15],[1,3,3,1]],
            "expected": 7 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == gridGame(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
