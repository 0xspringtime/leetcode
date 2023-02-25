def intervalIntersection(firstList, secondList):
    if firstList == [] or secondList == []:
        return []

    res = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        l = max(firstList[i][0], secondList[j][0])
        r = min(firstList[i][1], secondList[j][1])

        if l <= r:
            res.append([l, r])

        if firstList[i][1] < secondList[j][1]:
            i += 1

        else:
            j += 1

    return res


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0, 2], [5, 10], [13, 23], [24, 25]],
            "input1": [[1, 5], [8, 12], [15, 24], [25, 26]],
            "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        },
        {
            "name": "simple case 2",
            "input": [[1, 3], [5, 9]],
            "input1": [],
            "expected": []
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == intervalIntersection(test_case["input"], test_case["input1"]), test_case["name"]


if __name__ == "__main__":
    from datetime import datetime

    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
