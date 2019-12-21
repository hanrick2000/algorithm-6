public class Solution {
    /**
     * @param A: an integer array
     * @return: nothing
     */
    public void sortIntegers2(int[] A) {
        // write your code here
        if (A == null || A.length < 2) return;

        quickSort(A, 0, A.length - 1);
    }

    private void quickSort(int[] A, int start, int end) {
        if (start >= end) return;

        int pivot = partition(A, start, end);
        quickSort(A, start, pivot - 1);
        quickSort(A, pivot + 1, end);
    }

    private int partition(int[] A, int start, int end) {
        int pivot = A[end], i = start - 1;

        for (int j = start; j < end; j++) {
            if (A[j] <= pivot) {
                i++;
                if (j != i) {
                    swap(A, i, j);
                }
            }
        }

        swap(A, ++i, end);
        return i;
    }

    private void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}
