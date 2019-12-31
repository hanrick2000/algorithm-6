public class Solution {
    /**
     * @param n: An integer
     * @param edges: a list of undirected edges
     * @return: true if it's a valid tree, or false
     */
    public boolean validTree(int n, int[][] edges) {
        // write your code here
        if (n == 0 || n - 1 != edges.length) return false;

        Map<Integer, Set<Integer>> graph = initializeGraph(n, edges);

        Queue<Integer> q = new LinkedList<>();
        Set<Integer> set = new HashSet<>();

        q.offer(0);
        set.add(0);

        while (!q.isEmpty()) {
            int node = q.poll();
            for (Integer neighbor: graph.get(node)) {
                if (set.contains(neighbor)) continue;

                set.add(neighbor);
                q.offer(neighbor);
            }
        }

        return set.size() == n;
    }

    private Map<Integer, Set<Integer>> initializeGraph(int n, int[][] edges) {
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new HashSet<>());
        }

        for (int[] edge: edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        return graph;
    }
}
