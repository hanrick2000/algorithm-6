public class Solution {
    /**
     * @param A: an integer array
     * @param target: An integer
     * @param k: An integer
     * @return: an integer array
     */
    public int[] kClosestNumbers(int[] A, int target, int k) {
        // write your code here
        int r = findFirstIndex(A, target), l = r - 1;
        int[] result = new int[k];

        for (int i = 0; i < k; i++) {
            if (isLeftClosest(A, target, l, r)) {
                result[i] = A[l--];
            } else {
                result[i] = A[r++];
            }
        }

        return result;
    }

    private boolean isLeftClosest(int[] arr, int target, int left, int right) {
        if (left < 0) return false;
        if (right == arr.length) return true;

        return (target - arr[left] <= arr[right] - target);
    }

    private int findFirstIndex(int[] arr, int target) {
        int l = 0, r = arr.length - 1;

        while (l + 1 < r) {
            int mid = l + (r - l) / 2;

            if (arr[mid] >= target) {
                r = mid;
            } else {
                l = mid;
            }
        }

        if (arr[l] >= target) return l;
        if (arr[r] >= target) return r;

        return arr.length;
    }
}
