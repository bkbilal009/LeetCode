class Solution:
    def largestAltitude(self, gain):
        curAlt = 0
        maxAlt = curAlt

        for g in gain:
            curAlt += g
            if curAlt > maxAlt:
                maxAlt = curAlt

        return maxAlt
