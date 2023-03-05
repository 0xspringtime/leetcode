[?1000h[?1049h[?1h=[1;23r[27m[24m[23m[0m[H[2J[?25l[22;1H"testing1.py" 29L, 708B[1;1H[38;5;130m  1 def[0m [36maverage[0m(L):
[38;5;130m  2 
  3 
  4 def[0m [36mtest[0m():
[38;5;130m  5 [0m    test_cases = [
[38;5;130m  6 [0m[8C{
[38;5;130m  7 [0m[12C[31m"name"[0m: [31m"simple case 1"[0m,
[38;5;130m  8 [0m[12C[31m"input"[0m: [[31m1[0m, [31m2[0m, [31m3[0m],
[38;5;130m  9 [0m[12C[31m"input1"[0m: [31m2[0m,
[38;5;130m 10 [0m[12C[31m"expected"[0m: [31m2.0[0m
[38;5;130m 11 [0m[8C},
[38;5;130m 12 [0m[8C{
[38;5;130m 13 [0m[12C[31m"name"[0m: [31m"simple case 2"[0m,
[38;5;130m 14 [0m[12C[31m"input"[0m: [[31m1[0m, [31m2[0m, [31m3[0m, [31m4[0m],
[38;5;130m 15 [0m[12C[31m"input1"[0m: [31m3[0m,
[38;5;130m 16 [0m[12C[31m"expected"[0m: [31m2.5[0m
[38;5;130m 17 [0m[8C},
[38;5;130m 18 [0m    ]
[38;5;130m 19 
 20 [0m    [38;5;130mfor[0m test_case [38;5;130min[0m test_cases:
[1m[7mtesting1.py                                                  1,1            Top]0;testing1.py (~/lc) - VIM[1;5H[?25h[23;1H[?1000l]0;st[0m[22;1H[K[23;1H[?1l>[?1049ldef average(L):


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "input1": 2,
            "expected": 2.0
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "input1": 3,
            "expected": 2.5
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
def average(L):


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "input1": 2,
            "expected": 2.0
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "input1": 3,
            "expected": 2.5
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == average(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
