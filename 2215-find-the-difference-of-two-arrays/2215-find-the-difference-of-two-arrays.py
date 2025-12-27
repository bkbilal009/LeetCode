class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
         container1 = set(nums1)
         container2 = set(nums2)

         ans1 = []
         ans2 = []

         for num in container1:
             if num not in container2:
                 ans1.append(num)

         for num in container2:
             if num not in container1:
                 ans2.append(num)

         return [ans1, ans2]