from typing import List
def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

def test():
    test_cases = [
        {
            "name": "simple case 1",
            "input": 2,
            "input1": [[1,0]],
            "expected": [0,1] 
        },
        {
            "name": "simple case 2",
            "input": 4,
            "input1": [[1,0],[2,0],[3,1],[3,2]],
            "expected": [0,1,2,3] 
        },
    ]

    for test_case in test_cases:
        assert test_case["expected"] == findOrder(test_case["input"], test_case["input1"]), test_case["name"]

if __name__ == "__main__":
    from datetime import datetime
    start_time = datetime.now()
    print(findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
    test()
    print("Everything passed")
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
