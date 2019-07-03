# 1 - Defeat the Algorithm Interview

## Required (4)

### Easy  627. Longest Palindrome
https://www.lintcode.com/problem/longest-palindrome/

#### Description

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Assume the length of given string will not exceed 1010.

#### Example
##### Example 1:

    Input : s = "abccccdd"
    Output : 7
    Explanation :
    One longest palindrome that can be built is "dccaccd", whose length is `7`.

#### Notice
    Assume the length of given string will not exceed 1010.


### Easy  13. Implement strStr()
https://www.lintcode.com/problem/implement-strstr/

#### Description

For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

#### Clarification
Do I need to implement KMP Algorithm in a real interview?

* Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.

#### Example
##### Example 1:

    Input: source = "source" ，target = "target"
    Output: -1
    Explanation: If the source does not contain the target content, return - 1.
##### Example 2:

    Input:source = "abcdabcdefg" ，target = "bcd"
    Output: 1
    Explanation: If the source contains the target content, return the location where the target first appeared in the source.

#### Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)


### Medium  415. Valid Palindrome
https://www.lintcode.com/problem/valid-palindrome

#### Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

#### Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

#### Challenge
O(n) time without extra memory.

### Medium  200. Longest Palindromic Substring
https://www.lintcode.com/problem/longest-palindromic-substring/

#### Description

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

#### Example
##### Example 1:

    Input:"abcdzdcab"
    Output:"cdzdc"

##### Example 2:

    Input:"aba"
    Output:"aba"

#### Challenge
O(n2) time is acceptable. Can you do it in O(n) time.

## Optional (3)

### Medium  667. Longest Palindromic Subsequence

### Hard  841. String Replace

### Hard  594. strStr II
http://www.lintcode.com/problem/strstr-ii/

#### Description
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.

#### Example
Given source = abcdef, target = bcd, return 1.
