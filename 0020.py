def isValid(s: str) -> bool:
    Map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for c in s:
        if c not in Map:
            stack.append(c)
            continue
        if not stack or stack[-1] != Map[c]:
            return False
        stack.pop()

    return not stack

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": "()",
            "expected": True
        },
        {
            "name": "simple case 2",
            "input": "()[]{}",
            "expected": True
        },
        {
            "name": "simple case 3",
            "input": "(]",
            "expected": False
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isValid(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))