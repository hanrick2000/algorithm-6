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
        stack.push(root);
        while (!stack.isEmpty()) {
            UndirectedGraphNode node = stack.pop();
            result.add(node.label);

            for (int i = node.neighbors.size() - 1; i >= 0; i--) {
                stack.push(node.neighbors.get(i));
            }
        }

        return result;
    }
}
