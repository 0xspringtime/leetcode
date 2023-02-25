def evalRPN(tokens) -> int:
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["2","1","+","3","*"],
            "expected": 9
        },
        {
            "name": "simple case 2",
            "input": ["4","13","5","/","+"],
            "expected": 6
        },
        {
            "name": "simple case 3",
            "input": ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
            "expected": 22
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == evalRPN(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
