def matrixReshape(mat, r: int, c: int):
    flatten = []
    new_mat = []
    for row in mat:
        for num in row:
            flatten.append(num)

    if r * c != len(flatten):  # when given parameters is NOT possible and legal
        return mat
    else:
        for row_index in range(r):
            new_mat.append(flatten[row_index * c: row_index * c + c])
        return new_mat

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,2],[3,4]],
            "input1": 1,
            "input2": 4,
            "expected": [[1,2,3,4]]
        },
        {
            "name": "simple case 2",
            "input": [[1,2],[3,4]],
            "input1": 2,
            "input2": 4,
            "expected": [[1,2],[3,4]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == matrixReshape(test_case["input"], test_case["input1"], test_case["input2"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))