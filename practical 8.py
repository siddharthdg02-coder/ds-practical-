class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root


def longest_path(root):
    if root is None:
        return 0
    return 1 + max(longest_path(root.left),
                   longest_path(root.right))


def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def swap(root):
    if root:
        root.left, root.right = root.right, root.left
        swap(root.left)
        swap(root.right)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Main Program
root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)

print("\nInorder Traversal:")
inorder(root)

print("\nLongest Path Length:", longest_path(root))
print("Minimum Value:", find_min(root))

key = int(input("\nEnter value to search: "))

if search(root, key):
    print("Element Found")
else:
    print("Element Not Found")

swap(root)

print("Inorder after Swapping:")
inorder(root)
print()
