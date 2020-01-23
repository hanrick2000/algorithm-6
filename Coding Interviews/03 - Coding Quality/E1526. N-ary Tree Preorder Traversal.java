/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<UndirectedGraphNode>();
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: the tree
     * @return: pre order of the tree
     */
    public List<Integer> preorder(UndirectedGraphNode root) {
        // write your code here
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;

        Stack<UndirectedGraphNode> stack = new Stack<>();

        // method 2
        helper(root, result);

        // method 1
        // stack.push(root);
        // while (!stack.isEmpty()) {
        //     UndirectedGraphNode node = stack.pop();
        //     result.add(node.label);

        //     for (int i = node.neighbors.size() - 1; i >= 0; i--) {
        //         stack.push(node.neighbors.get(i));
        //     }
        // }

        return result;
    }

    private void helper(UndirectedGraphNode root, List<Integer> result) {
        if (root == null) return;

        result.add(root.label);
        if (root.neighbors.size() > 0) helper(root.neighbors.get(0), result);

        for (int i = 1; i < root.neighbors.size(); i++) {
            helper(root.neighbors.get(i), result);
        }
    }
}
