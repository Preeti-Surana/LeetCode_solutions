class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zeroes = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            ans = max(ans, right - left)
        return ans
"""
Approach:-
Hum ek window maintain karte hain jisme maximum 1 zero ho. right pointer se window ko expand karte hain.
Agar nums[right] == 0 ho to zeroes++.
Jab zeroes > 1 ho jaye, tab left pointer ko aage badha kar window shrink karte hain.
Valid window (at most one zero) ke liye answer right - left hoga, kyunki ek element delete karna compulsory hai.
Time Complexity : O(n)
Space Complexity : O(1)
"""
