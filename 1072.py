import collections
def maxEqualRowsAfterFlips(matrix):
    patterns = collections.Counter()
    for row in matrix:
        patterns[tuple(row)] += 1
        flip = [1 - c for c in row]
        patterns[tuple(flip)] += 1
    return max(patterns.values())

def maxEqualRowsAfterFlips1(matrix):
        cache = collections.defaultdict(int)
        for row in matrix:
            vals = []
            trans = []
            for c in row:
                vals.append(c)
                trans.append(1 - c)
            cache[str(vals)] += 1
            cache[str(trans)] += 1
        return max(cache.values())

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [[0,1],[1,1]],
            "expected": 1
        },
        {
            "name": "simple case 2",
            "input": [[0,1],[1,0]],
            "expected": 2
        },
        {
            "name": "list with one item",
            "input": [[0,0,0],[0,0,1],[1,1,0]],
            "expected": 2
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == maxEqualRowsAfterFlips(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))