class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)       
            l2, r2 = expand(i, i + 1)   

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
"""
Approach:-
- Consider every index as the center of a palindrome.
- Expand in both directions while the characters match.
- Do this for both:
Odd-length palindromes (i, i)
Even-length palindromes (i, i+1)
- Store the longest palindrome found. Return it.

Time Complexity : O(n^2)
Space Complexity : O(1)
"""
