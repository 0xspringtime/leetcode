#DFS
class Solution:
    def goodNodes(self, root):
        # The count of good nodes
        self.count = 0

        # Function to perform depth-first search
        def dfs(node, max_value):
            if node is None: # If the node is None, we have reached a leaf node, so return
                return

            # If the current node's value is greater than or equal to the max_value,
            # it's a good node, so increment the count
            if node.val >= max_value:
                self.count += 1
                max_value = node.val

            # Perform depth-first search on the left and right children
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        # Start the depth-first search
        dfs(root, root.val)

        # Return the count of good nodes
        return self.count
#time O(n)
#space O(h)
