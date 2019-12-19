public class Stack {
    private List<Integer> data = new ArrayList<Integer>();
    /*
     * @param x: An integer
     * @return: nothing
     */
    public void push(int x) {
        // write your code here
        data.add(x);
    }

    /*
     * @return: nothing
     */
    public void pop() {
        // write your code here
        int size = data.size();
        if (size > 0) {
            data.remove(size - 1);
        }
    }

    /*
     * @return: An integer
     */
    public int top() {
        // write your code here
        int size = data.size();
        return data.get(size - 1);
    }

    /*
     * @return: True if the stack is empty
     */
    public boolean isEmpty() {
        // write your code here
        return data.size() == 0;
    }
}
