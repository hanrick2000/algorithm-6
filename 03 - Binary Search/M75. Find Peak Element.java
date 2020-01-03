public class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        // write your code here
        if (A == null || A.length == 0) return -1;

        int l = 0, r = A.length - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (A[mid] >= A[mid + 1]) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }
}
