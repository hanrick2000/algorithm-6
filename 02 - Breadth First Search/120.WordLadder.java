public class Solution {
    /*
     * @param start: a string
     * @param end: a string
     * @param dict: a set of string
     * @return: An integer
     */
    public int ladderLength(String start, String end, Set<String> dict) {
        // write your code here
        if (dict == null) return 0;
        if (start.equals(end)) return 1;

        dict.add(end);

        Set<String> set = new HashSet<>();
        set.add(start);
        Queue<String> q = new LinkedList<>();
        q.offer(start);

        int distance = 1;
        while (!q.isEmpty()) {
            distance++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String word = q.poll();
                if (word.equals(end)) return distance;

                for (String next: getNextWords(word, dict)) {
                    if (set.contains(next)) continue;
                    if (next.equals(end)) return distance;

                    set.add(next);
                    q.offer(next);
                }
            }
        }

        return 0;
    }

    private List<String> getNextWords(String word, Set<String> dict) {
        List<String> next = new ArrayList<>();

        for (String d: dict) {
            int count = 0;
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == d.charAt(i)) continue;
                count++;
            }
            if (count == 1) next.add(d);
        }

        return next;
    }

    // --------------------------------------------------------------------
    // private String replace(String s, int index, char c) {
    //     char[] chars = s.toCharArray();
    //     chars[index] = c;
    //     return new String(chars);
    // }

    // private List<String> getNextWords(String word, Set<String> dict) {
    //     List<String> nextWords = new ArrayList<String>();
    //     for (char c = 'a'; c <= 'z'; c++) {
    //         for (int i = 0; i < word.length(); i++) {
    //             if (c == word.charAt(i)) {
    //                 continue;
    //             }
    //             String nextWord = replace(word, i, c);
    //             if (dict.contains(nextWord)) {
    //                 nextWords.add(nextWord);
    //             }
    //         }
    //     }
    //     return nextWords;
    // }
}


// leetcode
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (wordList == null) return 0;
        if (beginWord.equals(endWord)) return 1;

        Set<String> set = new HashSet<>();
        set.add(beginWord);
        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);

        int distance = 1;
        while (!q.isEmpty()) {
            distance++;
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String word = q.poll();
                // if (word.equals(endWord)) return distance;

                for (String next: getNextWords(word, wordList)) {
                    if (set.contains(next)) continue;
                    if (next.equals(endWord)) return distance;

                    set.add(next);
                    q.offer(next);
                }
            }
        }

        return 0;
    }

    private List<String> getNextWords(String word, List<String> dict) {
        List<String> next = new ArrayList<>();

        for (String d: dict) {
            int count = 0;
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == d.charAt(i)) continue;
                count++;
            }
            if (count == 1) next.add(d);
        }

        return next;
    }
}
