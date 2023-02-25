def minMeetingRooms(intervals):
    start = sorted([i[0] for i in intervals])
    end = sorted([i[1] for i in intervals])

    res, count = 0,0
    s,e = 0,0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)
    return res

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [(0,30),(5,10),(15,20)],
            "expected": 2
        },
        {
            "name": "simple case 2",
            "input": [(2,7)],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == minMeetingRooms(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))