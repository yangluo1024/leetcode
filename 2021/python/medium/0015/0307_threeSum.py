class Solution:
    # 双指针，time:N**2
    def threeSum(self, nums):
        res = []
        if len(nums) < 3: return res
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0: return res
            if i > 0 and nums[i] == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0: r -= 1
                elif s < 0: l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
        return res


