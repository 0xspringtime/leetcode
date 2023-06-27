#DFS
def combinationSum2(candidates, target):
    # the result array to store all combinations
    res = []
    candidates.sort()  # sort the candidates

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
            # skip the same element to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i-1]:
                continue
            # start from the next position because each number can only be used once
            dfs(target - candidates[i], path + [candidates[i]], i + 1)

    # start the dfs
    dfs(target, [], 0)

    return res
#time O(n^2)
#space O(target)
