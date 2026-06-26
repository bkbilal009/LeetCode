class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        pref = [0] * n
        
        # Step 1: Compute prefix sums where target is 1 and others are -1
        for i in range(n):
            pref[i] = 1 if nums[i] == target else -1
            if i > 0:
                pref[i] += pref[i - 1]
        
       
        unique_vals = sorted(list(set(pref + [0])))
        
        # Map values to 1-based ranks for the Fenwick Tree
        rank = {val: idx + 1 for idx, val in enumerate(unique_vals)}
        
        # Fenwick Tree (Binary Indexed Tree) helper functions
        bit_size = len(unique_vals)
        bit = [0] * (bit_size + 1)
        
        def update(idx: int, val: int):
            while idx <= bit_size:
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        # Step 3: Count valid subarrays
        ans = 0
        
        # st.insert({0, 0}) equivalent (insert rank of 0)
        update(rank[0], 1)
        
        for i in range(n):
            current_pref = pref[i]
            
            target_rank = rank[current_pref] - 1
            
            ans += query(target_rank)
            
            update(rank[current_pref], 1)
            
        return ans

        # Time Complexity: O(n \log n)
        # Space Complexity: $O(n)