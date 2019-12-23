public class Solution {
    /*
     * @param num: An integer
     * @return: An integer
     */
    public int countOnes(int num) {
        // write your code here
        int count = 0;
        while (num != 0) {
            num &= num - 1;
            count++;
        }

        return count;
    }
};
