public class Solution {
    /**
     * @param pattern: a string, denote pattern string
     * @param teststr: a string, denote matching string
     * @return: an boolean, denote whether the pattern string and the matching string match or not
     */
    public boolean wordPattern(String pattern, String teststr) {
        // write your code here
        String[] words = teststr.split(" ");

        if (words.length != pattern.length()) return false;

        Map<Character, String> hashmap = new HashMap<Character, String>();
        for (int i = 0; i < words.length; i++) {
            if (!hashmap.containsKey(pattern.charAt(i))) {
                if (hashmap.containsValue(words[i])) return false;
                hashmap.put(pattern.charAt(i), words[i]);
            } else if (!words[i].equals(hashmap.get(pattern.charAt(i))))
                return false;
        }

        return true;
    }
}
