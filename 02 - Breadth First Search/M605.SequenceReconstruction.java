public class Solution {
    /**
     * @param org: a permutation of the integers from 1 to n
     * @param seqs: a list of sequences
     * @return: true if it can be reconstructed only one or false
     */
    public boolean sequenceReconstruction(int[] org, int[][] seqs) {
        // write your code here
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();

        for (int num: org) {
            graph.put(num, new HashSet<>());
            indegree.put(num, 0);
        }

        int n = org.length, m = 0;
        for (int[] seq: seqs) {
            m += seq.length;
            if (seq.length >= 1 && (seq[0] <= 0 || seq[0] > n)) return false;

            for (int i = 1; i < seq.length; i++) {
                if (seq[i] <= 0 || seq[i] > n) return false;

                if (graph.get(seq[i - 1]).add(seq[i])) {
                    indegree.put(seq[i], indegree.get(seq[i]) + 1);
                }
            }
        }

        if (m < n) return false;

        Queue<Integer> q = new LinkedList<>();
        for (int key: indegree.keySet()) {
            if (indegree.get(key) == 0) q.offer(key);
        }

        int count = 0;
        while (q.size() == 1) {
            int num = q.poll();
            for (int next: graph.get(num)) {
                indegree.put(next, indegree.get(next) - 1);
                if (indegree.get(next) == 0) q.offer(next);
            }

            if (num != org[count++]) return false;
        }

        return count == n;
    }
}
