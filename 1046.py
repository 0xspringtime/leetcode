from typing import List
import heapq
def lastStoneWeight(stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])
def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [2,7,4,1,8,1],
            "expected": 1 
        },
        {
            "name": "simple case 2",
            "input": [1],
            "expected": 1
        }
    ]

    for test_case in test_cases:
        assert test_case["expected"] == lastStoneWeight(test_case["input"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))

