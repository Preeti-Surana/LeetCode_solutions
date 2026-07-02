class Solution(object):
    def isSubsequence(self, s, t):
        i = 0

        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)
""" 
Approach:-
- Use a pointer i for string s.
- Traverse string t character by character.
- If the current character in t matches s[i], move i to the next character.
- After traversing t, if i reaches the end of s, then s is a subsequence of t; otherwise, it is not.

Time Complexity: O(n)
Space Complexity: O(1)
"""
