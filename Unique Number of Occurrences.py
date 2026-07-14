class Solution(object):
    def uniqueOccurrences(self, arr):
        freq = {}
        for num in arr:  # Count frequency of each number
            freq[num] = freq.get(num, 0) + 1
        occurrences = list(freq.values())       # Get all frequencies

        return len(occurrences) == len(set(occurrences))  # Check if frequencies are unique
"""
Time Complexity : O(n)
Space Complexity : O(n)
"""
