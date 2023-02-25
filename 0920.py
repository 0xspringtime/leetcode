def canAttendMeetings(intervals):
    intervals.sort(key = lambda i: i[0])

    for i in range(1, len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]

        if i1[1] > i2[0]:
            return False
    return True
#O(nlogn)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [(0,30),(5,10),(15,20)],
            "expected": False
        },
        {
            "name": "simple case 2",
            "input": [(5,8),(9,15)],
            "expected": True
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == canAttendMeetings(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
