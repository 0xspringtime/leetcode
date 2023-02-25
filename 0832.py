def flipAndInvertImage(image):
    return [[1 - i for i in row[::-1]] for row in image]

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,1,0],[1,0,1],[0,0,0]],
            "expected": [[1,0,0],[0,1,0],[1,1,1]]
        },
        {
            "name": "simple case 2",
            "input": [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]],
            "expected": [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == flipAndInvertImage(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))