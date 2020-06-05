class Solution {
public:
    /**
     * @param pattern: a string,denote pattern string
     * @param str: a string, denote matching string
     * @return: a boolean
     */
    bool wordPatternMatch(string &pattern, string &str) {
        // write your code here
        unordered_map<char, string> mp;
        unordered_set<string> used;

        return isMatch(pattern, str, mp, used);
    }

    bool isMatch(const string &pattern, const string &str, unordered_map<char, string> mp, unordered_set<string> used) {
        if (pattern.length() == 0) return str.length() == 0;

        char ch = pattern[0];
        if (mp.count(ch) > 0) {
            string word = mp[ch];

            if (str.substr(0, word.length()) != word) return false;

            return isMatch(pattern.substr(1), str.substr(word.length()), mp, used);
        }

        for (int i = 0; i < str.length(); i++) {
            string word = str.substr(0, i + 1);
            if (used.count(word) > 0) continue;

            used.insert(word);
            mp[ch] = word;

            if (isMatch(pattern.substr(1), str.substr(i + 1), mp, used)) return true;

            mp.erase(ch);
            used.erase(word);
        }

        return false;
    }
};
