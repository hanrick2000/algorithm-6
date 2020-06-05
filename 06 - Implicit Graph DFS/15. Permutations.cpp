class Solution {
public:
    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int>> permute(vector<int> &nums) {
        // write your code here
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;

        bool next = true;
        while (next) {
            vector<int> permutation;
            for (int num: nums) permutation.push_back(num);
            result.push_back(permutation);

            next = nextPermutaion(nums);
        }

        return result;
    }

    bool nextPermutaion(vector<int> &nums) {
        int i = nums.size() - 1;
        while (i > 0 && nums[i] <= nums[i - 1]) i--;

        if (i <= 0) return false;

        int j = nums.size() - 1;
        while (nums[j] <= nums[i - 1]) j--;

        swap(nums[j], nums[i - 1]);

        j = nums.size() - 1;
        while (i < j) {
            swap(nums[i++], nums[j--]);
        }
    }
};
