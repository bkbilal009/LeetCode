class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        import heapq


class SegmentTree:

    def __init__(self, nums, flag):

        self.isMinTree = flag
        self.segmentTree = [0] * (4 * len(nums))

        self.build(0, 0, len(nums) - 1, nums)

    def build(self, i, l, r, nums):

        if l == r:
            self.segmentTree[i] = nums[l]
            return

        mid = (l + r) // 2

        self.build(2 * i + 1, l, mid, nums)
        self.build(2 * i + 2, mid + 1, r, nums)

        if self.isMinTree:
            self.segmentTree[i] = min(
                self.segmentTree[2 * i + 1],
                self.segmentTree[2 * i + 2]
            )
        else:
            self.segmentTree[i] = max(
                self.segmentTree[2 * i + 1],
                self.segmentTree[2 * i + 2]
            )

    def queryTree(self, start, end, i, l, r):

        # No overlap
        if l > end or r < start:
            return float('inf') if self.isMinTree else float('-inf')

        # Complete overlap
        if start <= l and r <= end:
            return self.segmentTree[i]

        mid = (l + r) // 2

        left = self.queryTree(start, end, 2 * i + 1, l, mid)
        right = self.queryTree(start, end, 2 * i + 2, mid + 1, r)

        if self.isMinTree:
            return min(left, right)

        return max(left, right)

    def query(self, l, r, n):
        return self.queryTree(l, r, 0, 0, n - 1)


class Solution:

    def getValue(self, l, r, minST, maxST, n):

        minEl = minST.query(l, r, n)
        maxEl = maxST.query(l, r, n)

        return maxEl - minEl

    def maxTotalValue(self, nums, k):

        n = len(nums)

        minST = SegmentTree(nums, True)
        maxST = SegmentTree(nums, False)

        pq = []

        # Initialize heap
        for l in range(n):

            value = self.getValue(l, n - 1, minST, maxST, n)

            heapq.heappush(pq, (-value, l, n - 1))

        result = 0

        while k:

            value, l, r = heapq.heappop(pq)

            value = -value

            result += value

            if r - 1 >= l:

                nextValue = self.getValue(
                    l,
                    r - 1,
                    minST,
                    maxST,
                    n
                )

                heapq.heappush(
                    pq,
                    (-nextValue, l, r - 1)
                )

            k -= 1

        return result