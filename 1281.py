def sum(n: int):
    return eval('*'.join(str(n))) - eval('+'.join(str(n)))

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 234,
            "expected": 15 
        },
        {
            "name": "simple case 2",
            "input": 4421,
            "expected": 21
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == sum(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
