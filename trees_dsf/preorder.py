class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def preorder(root):
    stack = [root]  # Initialize the stack with the root node
    traversed = []

    while stack:
        current = stack.pop()
        
        if current:
            traversed.append(current.val)

            # Push the right and left children onto the stack in reverse order (preorder)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    for value in traversed:
        print(value)

root = Node("A")
root.left = Node("F")
root.left.left = Node("Y")
root.right = Node("K")
root.right.right = Node("T")
root.left.right = Node("X")

preorder(root)
