class Solution:

    def findFinishTime(self, start1, duration1, start2, duration2):

        finish1 = float('inf')
        for i in range(len(start1)):
            finish1 = min(finish1, start1[i] + duration1[i])

        finish2 = float('inf')
        for i in range(len(start2)):
            finish2 = min(finish2, max(finish1, start2[i]) + duration2[i])

        return finish2

    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):

        pehleLand_FirWater = self.findFinishTime(
            landStartTime,
            landDuration,
            waterStartTime,
            waterDuration
        )

        pehleWater_FirLand = self.findFinishTime(
            waterStartTime,
            waterDuration,
            landStartTime,
            landDuration
        )

        return min(pehleLand_FirWater, pehleWater_FirLand)