public class Solution {
    /**
     * @param matrix: matrix, a list of lists of integers
     * @param target: An integer
     * @return: a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) return false;

        int row = matrix.length, col = matrix[0].length;
        int l = 0, r = row * col - 1;

        // methpd 2: check once
        // while (l <= r) {
        //     int mid = l + (r - l) / 2;
        //     int x = mid / col, y = mid % col;
        //     if (matrix[x][y] == target) return true;
        //     if (matrix[x][y] < target) {
        //         l = mid + 1;
        //     } else {
        //         r = mid - 1;
        //     }
        // }

        // return false;

        // method 1: check third times
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            int x = mid / col, y = mid % col;
            if (matrix[x][y] < target) {
                l = mid;
            } else {
                r = mid;
            }
        }

        return isMatch(matrix, l, col, target) || isMatch(matrix, r, col, target);
    }

    private boolean isMatch(int[][] matrix, int position, int col, int target) {
        int x = position / col, y = position % col;
        return matrix[x][y] == target;
    }
}
