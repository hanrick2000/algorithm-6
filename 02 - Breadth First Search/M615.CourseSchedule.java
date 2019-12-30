public class Solution {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // write your code here
        List[] edges = new ArrayList[numCourses];
        int[] degree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            edges[i] = new ArrayList<Integer>();
        }

        for (int[] sites: prerequisites) {
            edges[sites[1]].add(sites[0]);
            degree[sites[0]]++;
        }

        Queue q = new LinkedList();
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                q.offer(i);
            }
        }

        int count = 0;
        while (!q.isEmpty()) {
            int course = (int) q.poll();
            count++;

            int size = edges[course].size();
            for (int i = 0; i < size; i++) {
                int site = (int) edges[course].get(i);
                degree[site]--;
                if (degree[site] == 0) {
                    q.offer(site);
                }
            }
        }

        return count == numCourses;
    }
}
