from TreeNode import TreeNode


class Solution_226:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root


if __name__ == '__main__':
    root = TreeNode(4)
    node2 = TreeNode(2)
    node7 = TreeNode(7)
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)

    root.left = node2
    root.right = node7
    node2.left = node1
    node2.right = node3
    node7.left = node6
    node7.right = node9

    print([root.left.val, root.right.val])
    print([root.left.left.val, root.left.right.val] + [root.right.left.val, root.right.right.val])

    Solution_226().invertTree(root)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print([root.left.val, root.right.val])
    print([root.left.left.val, root.left.right.val] + [root.right.left.val, root.right.right.val])

