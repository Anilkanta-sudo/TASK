class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findPath(root, path, k):
    # Baes Case
    if root is None:
        return False

    path.append(root.key)

    # See if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False


def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)

print("LCA(1, 5) = %d" % (findLCA(root, 1, 5)))
print("LCA(3, 6) = %d" % (findLCA(root, 3, 6)))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
