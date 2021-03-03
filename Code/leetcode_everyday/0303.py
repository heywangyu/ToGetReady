# coding   : utf-8 
# @Time    : 21/03/03 8:24
# @Author  : Wang Yu
# @Project : ToGetReady
# @File    : 0303.py
# @Software: PyCharm


from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        338
        给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
        计算其二进制数中的 1 的数目并将它们作为数组返回。

        :param num:2
        :return:[0,1,1]
        造了个数组找规律
        i = 1, hammingWeight(i) = 1, i & (i - 1)=0
        i = 2, hammingWeight(i) = 1, i & (i - 1)=0
        i = 3, hammingWeight(i) = 2, i & (i - 1)=2
        i = 4, hammingWeight(i) = 1, i & (i - 1)=0
        i = 5, hammingWeight(i) = 2, i & (i - 1)=4
        i = 6, hammingWeight(i) = 2, i & (i - 1)=4
        i = 7, hammingWeight(i) = 3, i & (i - 1)=6
        i = 8, hammingWeight(i) = 1, i & (i - 1)=0
        i = 9, hammingWeight(i) = 2, i & (i - 1)=8
        i = 10, hammingWeight(i) = 2, i & (i - 1)=8
        i = 11, hammingWeight(i) = 3, i & (i - 1)=10
        i = 12, hammingWeight(i) = 2, i & (i - 1)=8
        i = 13, hammingWeight(i) = 3, i & (i - 1)=12
        i = 14, hammingWeight(i) = 3, i & (i - 1)=12
        i = 15, hammingWeight(i) = 4, i & (i - 1)=14
        i = 16, hammingWeight(i) = 1, i & (i - 1)=0
        i = 17, hammingWeight(i) = 2, i & (i - 1)=16
        i = 18, hammingWeight(i) = 2, i & (i - 1)=16
        i = 19, hammingWeight(i) = 3, i & (i - 1)=18

        """
        res = [0] * (num + 1)
        for digit in range(1, num + 1):
            tmp = digit & (digit - 1)
            res[digit] = res[tmp] + 1
        return res

    def hammingWeight(self, n: int) -> int:
        """
        编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
        :param n:
        :return:
        """
        # 自与消除最后一位1
        res = 0
        while n != 0:
            n = n & (n - 1)
            res += 1
        return res

        # 移位统计每次的末位1
        # res = 0
        # while n != 0:
        #     res += n % 2
        #     n >>= 1
        # return res

    def maxPathSum(self, root: TreeNode) -> int:
        """
        124
        路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
        同一个节点在一条路径序列中 至多出现一次 。
        该路径 至少包含一个 节点，且不一定经过根节点。
        路径和 是路径中各节点值的总和。
        给你一个二叉树的根节点 root ，返回其 最大路径和 。
        :param root:
        :return:
        """

    def maxDepth(self, root: TreeNode) -> int:
        """
        剑指 Offer 55 - I. 二叉树的深度
        输入一棵二叉树的根节点，求该树的深度。
        从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
