# 7 - Permutation-based & Graph-based DFS

## Required

### Medium  425. Letter Combinations of a Phone Number

#### Description
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

![Cellphone](https://github.com/porrychen/algorithm/blob/master/7%20-%20Permutation-based%20&%20Graph-based%20DFS/425-Telephone-keypad.png?raw=true)

Although the above answer is in lexicographical order, your answer could be in any order you want.

#### Example
    Given "23"

    Return
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

### Medium  10. String Permutation II
https://www.lintcode.com/problem/string-permutation-ii

#### Description
Given a string, find all permutations of it without duplicates.

#### Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].

### Medium  34. N-Queens II
https://www.lintcode.com/problem/n-queens-ii

#### Description
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

#### Example
For n=4, there are 2 distinct solutions.

### Medium  33. N-Queens
https://www.lintcode.com/problem/n-queens

#### Description
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

#### Example
There exist two distinct solutions to the 4-queens puzzle:

    [
      // Solution 1
      [".Q..",
       "...Q",
       "Q...",
       "..Q."
      ],
      // Solution 2
      ["..Q.",
       "Q...",
       "...Q",
       ".Q.."
      ]
    ]

#### Challenge
Can you do it without recursion?

### Medium  16. Permutations II
https://www.lintcode.com/problem/permutations-ii

#### Description
Given a list of numbers with duplicate number in it. Find all unique permutations.

#### Example
For numbers [1,2,2] the unique permutations are:

    [
      [1,2,2],
      [2,1,2],
      [2,2,1]
    ]

#### Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!

### Medium  15. Permutations
https://www.lintcode.com/problem/permutations

#### Description
Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

#### Example
For nums = [1,2,3], the permutations are:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

#### Challenge
Do it without recursion.

### Hard  829. Word Pattern II
https://www.lintcode.com/problem/word-pattern-ii

#### Description
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.

#### Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.

### Hard  132. Word Search II
https://www.lintcode.com/problem/word-search-ii

#### Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word. No same word in dictionary

#### Example
Given matrix:
    doaf
    agai
    dcan
and dictionary:

    {"dog", "dad", "dgdg", "can", "again"}

    return {"dog", "dad", "can", "again"}

    dog:
    doaf
    agai
    dcan
    dad:

    doaf
    agai
    dcan
    can:

    doaf
    agai
    dcan
    again:

    doaf
    agai
    dcan

#### Challenge
Using trie to implement your algorithm.

### Hard  121. Word Ladder II
https://www.lintcode.com/problem/word-ladder-ii

#### Description
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
All words have the same length.
All words contain only lowercase alphabetic characters.

#### Example
Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]

Return
    [
      ["hit","hot","dot","dog","cog"],
      ["hit","hot","lot","log","cog"]
    ]

## Optional

### Medium  190. Next Permutation II
### Medium  198. Permutation Index II
### Medium  197. Permutation Index
### Medium  52. Next Permutation
### Medium  51. Previous Permutation
### Hard  634. Word Squares

## Related

### Easy  828. Word Pattern
### Easy  211. String Permutation
### Medium  123. Word Search
