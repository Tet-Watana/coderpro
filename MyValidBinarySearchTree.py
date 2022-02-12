#13時になったら答え合わせ

class Node(object):
    def __init__(self, object):
        self.node=object

class Solution:
    def __init__(self):
        pass
    def isValidBST(self, node):
        
        return node

node=Node(5)
node.left=Node(4)
node.right=Node(7)

print(node.right.node)
#print(Solution().isValidBST(node))




"""
#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False
"""
