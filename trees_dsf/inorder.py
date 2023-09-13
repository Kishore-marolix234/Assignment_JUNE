class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def inorder(root):
    stack = []
    current = root
    traversed = []

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            traversed.append(current.val)
            current = current.right
        else:
            break

    for value in traversed:
        print(value)

root = Node("A")
root.left = Node("F")
root.left.left = Node("Y")
root.right = Node("K")
root.right.right = Node("T")
root.left.right = Node("X")

inorder(root)
