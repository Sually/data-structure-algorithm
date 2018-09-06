# -*- coding: utf-8 -*-
from buildTree import Tree,Node


class S:
    def __init__(self):
        pass

    def isBlanceTree(self, root):
        if not root:
            return True

        if not root.left and not root.right:
            return True

        flag = True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            flag = False

        return self.isBlanceTree(root.left) and self.isBlanceTree(root.right) and flag

    def maxDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

if __name__=='__main__':
    T = Tree()
    for i in range(1,10):
        T.add(i)
    S = S()
    print 'Tree depth:',S.maxDepth(T.root)
    print 'Tree is blance?',S.isBlanceTree(T.root)
    T.root.left.left.right.left = Node(8)
    print 'New tree depth:',S.maxDepth(T.root)
    print 'New tree is blance?',S.isBlanceTree(T.root)
    nullT = Tree()
    print 'Null tree depth:',S.maxDepth(nullT.root)
    print 'Null tree is blance?',S.isBlanceTree(nullT.root)