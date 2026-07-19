from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2):
            return False

        c1 = Counter(word1)
        c2 = Counter(word2)

        if set(c1.keys()) != set(c2.keys()):
            return False

        return sorted(c1.values()) == sorted(c2.values())
"""
Approach:-
If the lengths are different, return false.
Count the frequency of each character in both strings.
Check that both strings contain the same set of characters.
Sort the frequency arrays and compare them.
If they are equal, return true; otherwise, return false.

Time Complexity : O(n)
Space Complexity : O(1)
"""
