class Solution:
    # 位运算，time: N
    def singleNumbers(self, nums):
        # 将nums中所有数值异或
        xor = functools.reduce(lambda x, y: x^y, nums)
        bit = xor & -xor
        a = b = 0
        for n in nums:
            if n & bit == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]

