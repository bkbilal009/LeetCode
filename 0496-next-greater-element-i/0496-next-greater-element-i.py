class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        stack.append(0)
        mp = {}

        for i in range(1, len(nums2)):
            while True:
                if not stack:
                    stack.append(i)
                    break

                idx = stack[-1]

                if nums2[i] > nums2[idx]:
                    mp[nums2[idx]] = nums2[i]
                    stack.pop()
                else:
                    stack.append(i)
                    break

        res = [0] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] in mp:
                res[i] = mp[nums1[i]]
            else:
                res[i] = -1

        return res