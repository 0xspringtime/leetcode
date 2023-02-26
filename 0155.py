def __init__(self):
    self.stack = []
    self.minStack = []

def push(self, val: int) -> None:
    self.stack.append(val)
    val = min(val, self.minStack[-1] if self.minStack else val)
    self.minStack.append(val)

def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

def top(self) -> int:
    return self.stack[-1]

def getMin(self) -> int:
    return self.minStack[-1]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": ["MinStack","push","push","push","getMin","pop","top","getMin"][[],[-2],[0],[-3],[],[],[],[]],
            "expected": [null,null,null,null,-3,null,0,-2]
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
