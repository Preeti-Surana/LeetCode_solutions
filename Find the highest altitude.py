class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        ans = 0
        for g in gain:
            altitude += g
            if altitude > ans:
                ans = altitude
        return ans
