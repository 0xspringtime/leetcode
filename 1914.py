def rotateGrid(grid, k):
    n = len(grid)
    m = len(grid[0])

    i, j = 0, 0
    bottom, right = n - 1, m - 1
    while i < n // 2 and j < m // 2:
        temp = []
        for x in range(j, right):
            temp.append(grid[i][x])
        for x in range(i, bottom):
            temp.append(grid[x][right])
        for x in range(right, j, -1):
            temp.append(grid[bottom][x])
        for x in range(bottom, i, -1):
            temp.append(grid[x][j])

        indx = 0
        for x in range(j, right):
            grid[i][x] = temp[(k + indx) % len(temp)]
            indx += 1
        for x in range(i, bottom):
            grid[x][right] = temp[(k + indx) % len(temp)]
            indx += 1
        for x in range(right, j, -1):
            grid[bottom][x] = temp[(k + indx) % len(temp)]
            indx += 1
        for x in range(bottom, i, -1):
            grid[x][j] = temp[(k + indx) % len(temp)]
            indx += 1

        i += 1
        j += 1
        bottom -= 1
        right -= 1
    return grid
#O(m*n)

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[40,10],[30,20]],
            "input1": 1,
            "expected": [[10,20],[40,30]]
        },
        {
            "name": "simple case 2",
            "input": [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
            "input1": 2,
            "expected": [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == rotateGrid(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))