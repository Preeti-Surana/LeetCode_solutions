class Solution(object):
    def maxOperations(self, nums, k):
        freq = {}
        count = 0

        for num in nums:
            target = k - num

            if freq.get(target, 0) > 0:
                count += 1
                freq[target] -= 1
            else:
                freq[num] = freq.get(num, 0) + 1

        return count
"""
Approach:-
- Use a HashMap to store the frequency of unpaired numbers.
- Traverse the array once.
- For each number, find its complement k - num.
- If the complement exists in the map, form a pair, increase the count, and decrease its frequency.
- Otherwise, store the current number in the map.
- Return the total number of pairs.

Time Complexity: O(n)
Space Complexity: O(n)
"""
