class Solution:
    def maxEqualFreq(self, nums):
        count = {}      
        freq = {}       
        ans = 0
        maxFreq = 0
        for i, num in enumerate(nums):
            if num in count:
                old = count[num]
                freq[old] -= 1
                if freq[old] == 0:
                    del freq[old]

            count[num] = count.get(num, 0) + 1
            new = count[num]

            freq[new] = freq.get(new, 0) + 1

            maxFreq = max(maxFreq, new)

            length = i + 1
            if maxFreq == 1:
                ans = length

            elif (freq.get(maxFreq, 0) == 1 and
                  freq.get(maxFreq - 1, 0) * (maxFreq - 1) + maxFreq == length):
                ans = length

            elif (freq.get(1, 0) == 1 and
                  freq.get(maxFreq, 0) * maxFreq + 1 == length):
                ans = length

        return ans
