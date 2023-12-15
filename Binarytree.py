class Node():
    def __int__(self ,data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree():

    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            root = Node(value)
        else:
            self._add(self.root,value)
    def _add(self, node, value):
        if value< node.data:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(node, value)
            else:
                node.right = Node(value)
    def search(self,val):
        if self.root:
            if self.root.data == val:
                return self.root
        else:
            self._search(self.root, val)
    def _search(self,node,val):
        if node.data == val:
            return node

        if val < node.data and node.left:

            self._search(node.left,val)

        if val > node.data and node.right:
                self.search(node.right,val)

    def delete(self, key):
        """ delete the node with the given key and return the
        root node of the tree """

        if self.key == key:
            # found the node we need to delete

            if self.right and self.left:

                # get the successor node and its parent
                [psucc, succ] = self.right._findMin(self)

                # splice out the successor
                # (we need the parent to do this)

                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                # reset the left and right children of the successor

                succ.left = self.left
                succ.right = self.right

                return succ

            else:
                # "easier" case
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.key > key:  # key should be in the left subtree
                if self.left:
                    self.left = self.left.delete(key)
                # else the key is not in the tree

            else:  # key should be in the right subtree
                if self.right:
                    self.right = self.right.delete(key)

        return self

    def _findMin(self, parent):
        if self.left:
            return self.left._findMin(self)
        else:
            return [parent, self]


def lowestCommonNode(root, p, q):
    if root is None:
        return None
    if root == p or root == q:
        return  root

    left = lowestCommonNode(root.left, p ,q)
    right = lowestCommonNode(root.right,p,q)

    if left and right:
        return  root

    if left is None and right:
        return  right
    if right is None and left:
        return  left






