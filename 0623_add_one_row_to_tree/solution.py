

# Definition for a binary tree node.
from itertools import chain
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None


# t: bfs 66

def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, root, None)

    curd = 1;
    q = [root]
    while True:
        if curd == depth - 1:
            for node in q:
                new_lf = TreeNode(val, node.left, None)
                new_rh = TreeNode(val, None, node.right)
                node.left = new_lf
                node.right = new_rh

            return root

        # t: 130
        # q = filter(lambda x: x, chain(*[[node.left, node.right] for node in q]))
        oldq = []
        for node in q:
            if node.left:
                oldq.append(node.left)
            if node.right:
                oldq.append(node.right)
        q = oldq
        curd += 1

# Improved bfs maybe?
def addOneRow1_2(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, root, None)

    q = [(root, 1)]
    while q:
        (node, curd) = q.pop()
        if curd == depth - 1:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        else:
            if node.left:
                q.append((node.left, curd + 1))
            if node.right:
                q.append((node.right, curd + 1))

    return root


# Rebuild tree 53
def addOneRow2(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        return TreeNode(val, root, None)
    targetd = depth - 1
    def build_tree(node: Optional[TreeNode], thisd: int) -> Optional[TreeNode]:
        if node is None:
            return node

        if thisd < targetd:
            node.left = build_tree(node.left, thisd + 1)
            node.right = build_tree(node.right, thisd + 1)
        elif thisd == targetd:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)

        return node

    return build_tree(root, 1)





if __name__ == '__main__':
    pass

