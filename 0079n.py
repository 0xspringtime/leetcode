#DFS
def exist(board, word):
    def dfs(board, i, j, word):
        # If we have found all the letters of the word, return True
        if len(word) == 0:
            return True

        # If we are out of bounds or the current cell doesn't have the letter that we are looking for, return False
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[0]:
            return False

        # Mark the current cell as visited
        temp = board[i][j]
        board[i][j] = '#'

        # Recurse on all the possible directions
        res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j+1, word[1:]) or dfs(board, i, j-1, word[1:])

        # Unmark the current cell
        board[i][j] = temp

        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True

    return False
#time O(MN4^L)
#space O(L)
