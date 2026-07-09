class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        max_len = 0
        zero_count = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len
"""
Approach:-
Use a sliding window that contains at most k zeros. Expand the window with right, shrink it with left whenever zeros exceed k, and 
keep track of the maximum valid window size.

Time Complexity:O(n)
Space Complexity: O(1)
"""
