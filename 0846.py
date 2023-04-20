from typing import List
import heapq
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1,2,3,6,2,3,4,7,8],
            "input1": 3,
            "expected": True 
        },
        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4, 5],
            "input1": 4444,
            "expected": False 
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == isNStraightHand(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
