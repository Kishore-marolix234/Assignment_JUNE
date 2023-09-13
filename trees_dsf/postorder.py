class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    traversed = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        traversed.append(stack2.pop().val)

    for value in traversed:
        print(value)

root = Node("A")
root.left = Node("F")
root.left.left = Node("Y")
root.right = Node("K")
root.right.right = Node("T")
root.left.right = Node("X")

postorder(root)
