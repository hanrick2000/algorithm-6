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
    /**
     * @param root: the binary tree of the  root
     * @return: return a list of double
     */
    public List<Double> averageOfLevels(TreeNode root) {
        // write your code here
        List<Double> result = new ArrayList<>();
        if (root == null) return result;

        // method 2
        List<Integer> count = new ArrayList<>();
        average(root, 0, result, count);

        for (int i = 0; i < result.size(); i++) {
            result.set(i, result.get(i) / count.get(i));
        }

        // method 1
        // Queue<TreeNode> q = new LinkedList<>();
        // q.offer(root);
        // while (!q.isEmpty()) {
        //     long sum = 0;
        //     int size = q.size();
        //     for (int i = 0; i < size; i++) {
        //         TreeNode node = q.poll();
        //         sum += node.val;
        //         if (node.left != null) q.offer(node.left);
        //         if (node.right != null) q.offer(node.right);
        //     }
        //     result.add(sum * 1.0 / size);
        // }

        return result;
    }

    private void average(TreeNode root, int level, List<Double> sum, List<Integer> count) {
        if (root == null) return;

        if (level < sum.size()) {
            sum.set(level, sum.get(level) + root.val);
            count.set(level, count.get(level) + 1);
        } else {
            sum.add(1.0 * root.val);
            count.add(1);
        }

        average(root.left, level + 1, sum, count);
        average(root.right, level + 1, sum, count);
    }
}
