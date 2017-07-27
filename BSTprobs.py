# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

# A function to do inorder tree traversal
def printInorder(root):
    if root:
        printInorder(root.left)
        print root.val
        printInorder(root.right)
 
# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print root.val
 
# A function to do postorder tree traversal
def printPreorder(root):
    if root:
        print root.val
        printPreorder(root.left)
        printPreorder(root.right)

def LevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        n = queue.pop(0)
        print n.val
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)

def MinDepth(root):
    if root is None:
        return
    queue = []
    queue.append({'node': root, 'depth': 1})
    while len(queue) > 0:
        item = queue.pop(0)
        node = item['node']
        depth = item['depth']
        if node.left is None and node.right is None:
            return depth
        if node.left:
            queue.append({'node': node.left, 'depth': depth + 1})
        if node.right:
            queue.append({'node': node.right, 'depth': depth + 1})


def MaxDepth(root):
    if root is None:
        return 0

    ld = MaxDepth(root.left)
    rd = MaxDepth(root.right)

    if ld > rd:
        return ld + 1
    else:
        return rd + 1

# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
print "Preorder traversal of binary tree is"
printPreorder(root)
 
print "\nInorder traversal of binary tree is"
printInorder(root)
 
print "\nPostorder traversal of binary tree is"
printPostorder(root)

print "\nLevelorder traversal of binary tree is"
LevelOrder(root)

print "\nMinDepth traversal of binary tree is"
print MinDepth(root)

print "\nMaxDepth traversal of binary tree is"
print MaxDepth(root)

