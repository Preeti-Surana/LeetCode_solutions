class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i  in range(len(nums)):
            right = total - left -nums[i]
            if(left == right):
                return i
            left = left+nums[i]
        return -1   

"""
Poore array ka total sum nikaal lo.
left variable ko 0 se initialize karo.
Har index i par:
right = total - left - nums[i]
Agar left == right, to wahi pivot index hai.
Warna left += nums[i] karke aage badho.
Agar poora loop khatam ho jaye aur koi index na mile, to -1 return karo.

Time Complexity: O(n)
Space Complexity: O(1)
"""
