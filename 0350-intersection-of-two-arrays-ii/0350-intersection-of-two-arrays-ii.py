class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []

        # Step 1: Count elements of nums1
        for num in nums1:
            count[num] = count.get(num, 0) + 1

        # Step 2: Traverse nums2 and build intersection
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result