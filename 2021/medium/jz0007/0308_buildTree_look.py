class Solution:
    # recursion & hash, time: N
    # inorder的left,right索引用于确定preorder的root索引
    # preorder的root索引用于确定根节点, 当所有节点全部遍历完，即树已建成
    def buildTree(self, preorder, inorder):
        def recursion(root, left, right):
            if left > right: return None
            node = TreeNode(preorder[root])
            idx = dic[node.val]
            node.left = recursion(root + 1, left, idx - 1)
            node.right = recursion(root + (idx - left) + 1, idx + 1, right)
            return node

        # 假设树中没有重复值
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        return recursion(0, 0, len(inorder) - 1)
        
