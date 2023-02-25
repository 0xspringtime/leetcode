def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    big = set()
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]!='.':
                cur = board[i][j]
                if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                    return False
                big.add((i,cur))
                big.add((cur,j))
                big.add((i/3,j/3,cur))
    return True
#O(1)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]],
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isValidSudoku(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
