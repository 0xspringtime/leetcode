from typing import List
def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    m, n = len(img), len(img[0])

    def avg(i, j):
        s = squares = 0
        top, bottom = max(0, i - 1), min(m, i + 2)
        left, right = max(0, j - 1), min(n, j + 2)

        for x in range(top, bottom):
            for y in range(left, right):
                s += img[x][y]
                squares += 1

        return s // squares

    return [[avg(i, j) for j in range(n)] for i in range(m)]


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,1,1],[1,0,1],[1,1,1]],
            "expected": [[0,0,0],[0,0,0],[0,0,0]] 
        },
        {
            "name": "simple case 2",
            "input": [[100,200,100],[200,50,200],[100,200,100]],
            "expected": [[137,141,137],[141,138,141],[137,141,137]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == imageSmoother(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
