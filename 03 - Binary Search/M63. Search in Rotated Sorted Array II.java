public class Solution {
    /**
     * @param A: an integer ratated sorted array and duplicates are allowed
     * @param target: An integer
     * @return: a boolean
     */
    public boolean search(int[] A, int target) {
        // write your code here

        // method 1
        for (int n: A) {
            if (n == target) return true;
        }

        return false;

        // method 2
        // if (A == null || A.length == 0) return false;

        // int l = 0, r = A.length - 1;
        // while (l + 1 < r) {
        //     int mid = l + (r - l) / 2;
        //     if (A[mid] == target) return true;
        //     if (A[mid] > A[l]) {
        //         if (A[mid] >= target && target >= A[l]) {
        //             r = mid;
        //         } else {
        //             l = mid;
        //         }
        //     } else if (A[mid] < A[l]) {
        //         if (A[mid] <= target && target <= A[r]) {
        //             l = mid;
        //         } else {
        //             r = mid;
        //         }
        //     } else {
        //         l++;
        //     }
        // }

        // return (A[l] == target || A[r] == target);
    }

}
