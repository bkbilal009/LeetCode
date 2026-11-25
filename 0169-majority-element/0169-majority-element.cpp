class Solution {
public:
    int majorityElement(vector<int>& nums) {

        int n = nums.size();

        int freq = 0, ans = 0;

        // Step 1: Find candidate
        for (int i = 0; i < n; i++) {

            if (freq == 0) {
                ans = nums[i];
            }

            if (ans == nums[i]) {
                freq++;
            }
            else {
                freq--;
            }
        }

        // Step 2: Verify candidate
        int count = 0;

        for (int val : nums) {
            if (val == ans) {
                count++;
            }
        }

        if (count > n / 2) {
            return ans;
        }

        return -1;
    }
};