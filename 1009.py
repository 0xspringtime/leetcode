def bitwiseComplement(n: int) -> int:
    s=bin(n).replace('0b','')
    t=''
    for i in s:
        if i=='0':
            t+='1'
        else:
            t+='0'
    return int(t,2)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 5,
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": 7,
            "expected": 0 
        },
        {
            "name": "case 3",
            "input": 10,
            "expected": 5 
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == bitwiseComplement(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
