class Solution {
public:
    /*
     * @param start: a string
     * @param end: a string
     * @param dict: a set of string
     * @return: a list of lists of string
     */
    vector<vector<string>> findLadders(string &start, string &end, unordered_set<string> &dict) {
        // write your code here
        vector<vector<string>> result;
        unordered_map<string, vector<string>> mp;
        unordered_map<string, int> distance;

        dict.insert(start);
        dict.insert(end);

        bfs(end, start, dict, distance, mp);

        vector<string> path;
        dfs(start, end, path, distance, mp, result);

        return result;
    }

    void dfs(const string &start, const string &end, vector<string> &path,
                unordered_map<string, int> &distance, unordered_map<string, vector<string>> &mp,
                vector<vector<string>> &result) {
        path.push_back(start);

        if (start == end) {
            result.push_back(path);
        } else {
            for (auto next: mp[start]) {
                if (distance.count(next) > 0 && distance[start] == distance[next] - 1) {
                    dfs(next, end, path, distance, mp, result);
                }
            }
        }

        path.pop_back();
    }

    void bfs(const string &end, const string &start, unordered_set<string> &dict,
                unordered_map<string, int> &distance, unordered_map<string, vector<string>> &mp) {
        queue<string> q;
        q.push(start);

        distance[start] = 0;

        while (!q.empty()) {
            string word = q.front();
            q.pop();

            vector<string> words = nextWords(word, dict);
            for (auto next: words) {
                mp[next].push_back(word);

                if (distance.count(next) == 0) {
                    distance[next] = distance[word] + 1;
                    q.push(next);
                }
            }
        }
    }

    vector<string> nextWords(string &word, unordered_set<string> &dict) {
        vector<string> result;

        for (int i = 0; i < word.length(); i++) {
            char tmp = word[i];
            for (char c = 'a'; c <= 'z'; c++) {
                if (tmp == c) continue;

                word[i] = c;
                if (dict.count(word) > 0) result.push_back(word);
            }
            word[i] = tmp;
        }

        return result;
    }
};
