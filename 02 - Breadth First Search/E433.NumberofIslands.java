public class Solution {
    /**
     * @param grid: a boolean 2D matrix
     * @return: an integer
     */
    public int numIslands(boolean[][] grid) {
        // write your code here
        if (grid == null || grid.length == 0 || grid[0] == null) return 0;

        int count = 0, col_size = grid[0].length;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < col_size; j++) {
                if (grid[i][j]) {
                    bfs(grid, i, j);
                    count++;
                }
            }
        }

        return count;
    }

    private void bfs(boolean[][] grid, int x, int y) {
        int[] dx = new int[]{0, 0, 1, -1};
        int[] dy = new int[]{1, -1, 0, 0};

        Queue<Integer> qx = new LinkedList<>();
        Queue<Integer> qy = new LinkedList<>();
        qx.offer(x);
        qy.offer(y);

        grid[x][y] = false;

        while (!qx.isEmpty()) {
            x = qx.poll();
            y = qy.poll();

            for (int i = 0; i < dx.length; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (!isValid(grid, nx, ny)) {
                    continue;
                }

                qx.offer(nx);
                qy.offer(ny);
                grid[nx][ny] = false;
            }
        }
    }

    private boolean isValid(boolean[][] grid, int x, int y) {
        int row_size = grid.length, col_size = grid[0].length;

        return x >= 0 && y >= 0 && x < row_size && y < col_size && grid[x][y];
    }
}

// leetcode
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null) return 0;

        int count = 0, col_size = grid[0].length;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < col_size; j++) {
                if (grid[i][j] == '1') {
                    bfs(grid, i, j);
                    count++;
                }
            }
        }

        return count;
    }

    private void bfs(char[][] grid, int x, int y) {
        int[] dx = new int[]{0, 0, 1, -1};
        int[] dy = new int[]{1, -1, 0, 0};

        Queue<Integer> qx = new LinkedList<>();
        Queue<Integer> qy = new LinkedList<>();
        qx.offer(x);
        qy.offer(y);

        grid[x][y] = '0';

        while (!qx.isEmpty()) {
            x = qx.poll();
            y = qy.poll();

            for (int i = 0; i < dx.length; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (!isValid(grid, nx, ny)) {
                    continue;
                }

                qx.offer(nx);
                qy.offer(ny);
                grid[nx][ny] = '0';
            }
        }
    }

    private boolean isValid(char[][] grid, int x, int y) {
        int row_size = grid.length, col_size = grid[0].length;

        return x >= 0 && y >= 0 && x < row_size && y < col_size && grid[x][y] == '1';
    }
}
