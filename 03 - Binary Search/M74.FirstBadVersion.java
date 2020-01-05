/**
 * public class SVNRepo {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use SVNRepo.isBadVersion(k) to judge whether
 * the kth code version is bad or not.
*/
public class Solution {
    /**
     * @param n: An integer
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        // write your code here
        int l = 1, r = n;
        method 1
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (SVNRepo.isBadVersion(mid)) {
                r = mid;
            } else {
                l = mid + 1;
            }
            System.out.println(l + ":" + r);
        }

        return l;

        // method 2
        // while (l + 1 < r) {
        //     int mid = l + (r - l) / 2;
        //     if (SVNRepo.isBadVersion(mid)) {
        //         r = mid;
        //     } else {
        //         l = mid;
        //     }
        // }

        // if (SVNRepo.isBadVersion(l)) return l;
        // return r;
    }
}
