# -*- coding: utf-8 -*-
# contain preorder inorder postorder level traversal function

from buildTree import Tree

class S:
    def __init__(self):
        pass

    def preorderTraversal(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))

        return res


    def inorderTraversal(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        res = []
        res.extend(self.inorderTraversal(root.left))
        res.extend([root.val])
        res.extend(self.inorderTraversal(root.right))

        return res


    def postorderTraversal(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        res = []
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.extend([root.val])

        return res


    def levelTraversal(self, root):
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        q = [root]
        res = []
        while len(q) > 0:
            popNode = q.pop(0)
            res.append(popNode.val)
            if popNode.left is not None:
                q.append(popNode.left)
            if popNode.right is not None:
                q.append(popNode.right)

        return res



if __name__=='__main__':
    T = Tree()
    for i in range(1,10,1):
        T.add(i)
    S = S()
    print 'preorderTraversal:',S.preorderTraversal(T.root)
    print 'inorderTraversal:',S.inorderTraversal(T.root)
    print 'postorderTraversal:',S.postorderTraversal(T.root)
    print 'levelTraversal:',S.levelTraversal(T.root)