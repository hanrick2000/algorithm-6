public class TwoSum {
    private Map<Integer, Integer> nums;

    TwoSum() {
        nums = new HashMap<Integer, Integer>();
    }

    /**
     * @param number: An integer
     * @return: nothing
     */
    public void add(int number) {
        // write your code here
        if (nums.containsKey(number))
            nums.put(number, nums.get(number) + 1);
        else
            nums.put(number, 1);
    }

    /**
     * @param value: An integer
     * @return: Find if there exists any pair of numbers which sum is equal to the value.
     */
    public boolean find(int value) {
        // write your code here
        for (Map.Entry item: nums.entrySet()) {
            int key = (int)item.getKey();
            if (nums.containsKey(value - key) && (value - key != key || (int)item.getValue() > 1)) return true;
        }

        return false;
    }
}
