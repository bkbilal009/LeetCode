class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if (slow == fast):
                break

        

        n1 = 0
        n2 = slow

        while (n1 != n2):
            n1 = nums[n1]
            n2 = nums[n2]

        return n1
