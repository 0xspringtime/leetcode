def numMagicSquaresInside(G) -> int:
    M, N, S, t, s = len(G), len(G[0]), set(range(1, 10)), range(3), 0
    for i in range(M - 2):
        for j in range(N - 2):
            g = [G[i + k][j:j + 3] for k in t]
            if set(sum(g, [])) != S or g[1][1] != 5: continue
            if any(sum(g[k]) != 15 for k in t) or any(sum([g[k][l] for k in t]) != 15 for l in t): continue
            if sum([g[k][k] for k in t]) != 15 or sum([g[k][2 - k] for k in t]) != 15: continue
            s += 1
    return s

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[8]],
            "expected": 0
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == numMagicSquaresInside(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))