public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        // write your code here
        int result = 0;
        if (matrix == null || matrix.length == 0 || matrix[0] == null || matrix[0].length == 0) return result;

        int col = matrix[0].length, x = matrix.length - 1, y = 0;
        while (x >= 0 && y < col) {
            if (matrix[x][y] == target) {
                result++;
                x--;
                y++;
            } else if (matrix[x][y] < target) {
                y++;
            } else {
                x--;
            }
        }

        return result;
    }
}
