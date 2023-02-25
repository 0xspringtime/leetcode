def floodFill(image, sr: int, sc: int, newColor: int):
    rows = len(image)
    cols = len(image[0])
    color_to_change = image[sr][sc]

    def dfs(r, c):
        nonlocal rows, cols, newColor, image

        if r < 0 or c < 0 or r > rows - 1 or c > cols - 1 or image[r][c] == newColor or image[r][c] != color_to_change:
            return

        image[r][c] = newColor

        # radiate in four directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)

    return image

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[1,1,1],[1,1,0],[1,0,1]],
            "input1": 1,
            "input2": 1,
            "input3": 2,
            "expected": [[2,2,2],[2,2,0],[2,0,1]]
        },
        {
            "name": "simple case 1",
            "input": [[0,0,0],[0,0,0]],
            "input1": 0,
            "input2": 0,
            "input3": 0,
            "expected": [[0,0,0],[0,0,0]]
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == floodFill(test_case["input"], test_case["input1"], test_case["input2"], test_case["input3"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))