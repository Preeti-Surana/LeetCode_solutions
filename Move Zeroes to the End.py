class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
      
""" Approach:-
- Keep a pointer j for the next non-zero position.
- Traverse the array with i.
- If nums[i] is non-zero, swap it with nums[j] and increment j.
- Non-zero elements move to the front, and zeros automatically shift to the end.
Time Complexity: O(n)
Space Complexity: O(1) """
