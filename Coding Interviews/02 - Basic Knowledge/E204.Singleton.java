class Solution {
    private static Solution instance = null;

    /**
     * @return: The same instance of this class every time
     */
    public static Solution getInstance() {
        // write your code here
        if (instance == null) {
            instance = new Solution();
        }

        return instance;
    }
};
