class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]

            if window_sum > max_sum:
                max_sum = window_sum

        return float(max_sum) / k
"""
Approach:- 
- Calculate the sum of the first k elements.
- Store it as the current maximum sum.
- Move the window one step at a time:
- Add the new element entering the window.
- Remove the element leaving the window.
- Update the maximum sum if the current window sum is larger.
- Return max_sum / k.

Time Complexity : O(n)
Space Complexity : O(1)

"""
