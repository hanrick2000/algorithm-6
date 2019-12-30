class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // List[] edges = new ArrayList[numCourses];
        Map<Integer, List<Integer>> edges = new HashMap<>();
        int[] degree = new int[numCourses];

        // for (int i = 0; i < numCourses; i++) {
        //     edges[i] = new ArrayList<Integer>();
        // }

        for (int[] pair: prerequisites) {
            int dest = pair[0], src = pair[1];

            List<Integer> preList = edges.getOrDefault(src, new ArrayList<>());
            preList.add(dest);
            edges.put(src, preList);

            degree[dest]++;
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                q.offer(i);
            }
        }

        int[] result = new int[numCourses];
        int count = 0;
        while (!q.isEmpty()) {
            int course = q.poll();
            result[count++] = course;
            if (!edges.containsKey(course)) continue;

            for (Integer dest: edges.get(course)) {
                degree[dest]--;
                if (degree[dest] == 0) {
                    q.offer(dest);
                }
            }
        }

        if (count == numCourses) {
            return result;
        }

        return new int[0];
    }
}
