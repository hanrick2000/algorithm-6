class Solution {
public:
    /**
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    vector<vector<int>> subsets(vector<int> &nums) {
        // write your code here
        sort(nums.begin(), nums.end());

        // method 2
        // vector<vector<int>> result;
        // vector<int> subset;

        // dfs(nums, 0, subset, result);

        // return result;

        // method 1
        vector<vector<int>> result;
        vector<int> empty;
        result.push_back(empty);

        for (int num: nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                vector<int> subset = result[i];
                subset.push_back(num);
                result.push_back(subset);
            }
        }

        return result;
    }

    void dfs(vector<int> &nums, int index, vector<int> &subset, vector<vector<int>> &result) {
        result.push_back(subset);

        for (int i = index; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            dfs(nums, i + 1, subset, result);
            subset.pop_back();
        }
    }
};
