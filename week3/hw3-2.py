class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = {'value': root_val, 'left': None, 'right': None}

    root_index = inorder.index(root_val)

    root['left'] = build_tree(preorder[1:1 + root_index], inorder[:root_index])
    root['right'] = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])

    return root

def calculate_height(node):
    if not node:
        return 0

    left_height = calculate_height(node['left'])
    right_height = calculate_height(node['right'])

    return max(left_height, right_height) + 1

import sys
input = sys.stdin.read
data = input().splitlines()

preorder = list(map(int, data[0].split()))
inorder = list(map(int, data[1].split()))

tree = build_tree(preorder, inorder)

print(calculate_height(tree))

