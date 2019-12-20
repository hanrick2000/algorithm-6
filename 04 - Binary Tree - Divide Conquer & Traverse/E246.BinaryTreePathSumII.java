/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /*
     * @param root: the root of binary tree
     * @param target: An integer
     * @return: all valid paths
     */
    public List<List<Integer>> binaryTreePathSum2(TreeNode root, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) return result;

        List<Integer> path = new ArrayList<Integer>();
        helper(root, target, path, result);

        return result;
    }

    private void helper(TreeNode root, int target, List<Integer> path, List<List<Integer>> result) {
        if (root == null) return;

        path.add(root.val);
        int sum = target;
        int level = path.size() - 1;

        for (int i = level; i >= 0; i--) {
            sum -= path.get(i);
            if (sum == 0) {
                result.add(new ArrayList<Integer>(path.subList(i, level + 1)));
            }
        }

        helper(root.left, target, path, result);
        helper(root.right, target, path, result);

        path.remove(level);
    }
}
