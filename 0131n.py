#DFS
def partition(s):
    # This function checks whether a string is a palindrome
    def is_palindrome(s):
        return s == s[::-1]

    # This function uses DFS to generate all possible partitions
    def dfs(s, path, res):
        if not s:  # If we've reached the end of the string
            res.append(path)
            return
        for i in range(1, len(s) + 1):  # For every substring in the string
            if is_palindrome(s[:i]):
                dfs(s[i:], path + [s[:i]], res)

    res = []
    dfs(s, [], res)
    return res
#time O(n*n^2)
#spacec O(n)
