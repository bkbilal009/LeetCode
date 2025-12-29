class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
         i = 0
         j = 0
         result = []

         while i < len(nums1) and j < len(nums2):
             id1 = nums1[i][0]
             id2 = nums2[j][0]

             if id1 == id2:
                 result.append([id1, nums1[i][1] + nums2[j][1]])
                 i += 1
                 j += 1

             elif id1 < id2:
                 result.append([id1, nums1[i][1]])
                 i += 1
             else:
                 result.append([id2, nums2[j][1]])
                 j += 1

         while i < len(nums1):
             result.append([nums1[i][0], nums1[i][1]])
             i += 1

         while j < len(nums2):
             result.append([nums2[j][0], nums2[j][1]])
             j += 1

         return result