class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            if count > max_count:
                max_count = count
        return max_count

"""
Approach:-
- Take the first substring of length k and count its vowels.
- Store this count as the current maximum.
- Move the window one step at a time:
- Add the new character entering the window.
- Subtract the character leaving the window.
- After each move, update the maximum vowel count.
- Return the maximum count obtained from all windows.

Time Complexity: O(n)
Space Compexity: O(1)
"""
