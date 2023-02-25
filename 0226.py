class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def invertTree(node):
  if node is None:
    return None

  node.left, node.right = node.right, node.left

  invertTree(node.left)
  invertTree(node.right)

  return node

sample_tree = TreeNode(1)
sample_tree.left = TreeNode(2)
sample_tree.right = TreeNode(3)
sample_tree.left.left = TreeNode(4)
sample_tree.left.right = TreeNode(5)
sample_tree.right.left = TreeNode(6)
sample_tree.right.right = TreeNode(7)

def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

def printTree(node):
  print(node.val, end="")
  if node.left:
    printTree(node.left)
  if node.right:
    printTree(node.right)
    
printTree(sample_tree)
inverted_tree = invertTree(sample_tree)
printTree(inverted_tree)
