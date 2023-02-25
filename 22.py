def generateParenthesis(n: int):
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 3,
            "expected": ["((()))","(()())","(())()","()(())","()()()"]
        },
        {
            "name": "simple case 2",
            "input": 1,
            "expected": ["()"]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == generateParenthesis(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))