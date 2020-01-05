public class Solution {
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    public int search(int[] A, int target) {
        // write your code here
        if (A == null || A.length == 0) return -1;

        int l = 0, r = A.length - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (A[mid] > A[l]) {
                if (A[mid] >= target && target >= A[l]) {
                    r = mid;
                } else {
                    l = mid;
                }
            } else {
                if (A[mid] <= target && target <= A[r]) {
                    l = mid;
                } else {
                    r = mid;
                }
            }
        }

        if (A[l] == target) return l;
        if (A[r] == target) return r;

        return -1;
    }
}
