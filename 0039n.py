#DFS
def combinationSum(candidates, target):
    # the result array to store all combinations
    res = []

    def dfs(target, path, start):
        # if target < 0, it means the current combination exceeds the target, so we return
        if target < 0:
            return
        # if target == 0, it means we find a valid combination, so we add it to the result
        elif target == 0:
            res.append(path)
            return
        # for each number, we try to subtract it from target and recursively find the next number
        for i in range(start, len(candidates)):
            dfs(target - candidates[i], path + [candidates[i]], i)

    # start the dfs
    dfs(target, [], 0)

    return res
#time O(n^(target/min))
#space O(target/min)
