# 20190101

## 891. Valid Palindrome II
https://www.lintcode.com/problem/valid-palindrome-ii

### Description
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

### Example
Given s = "aba" return true
Given s = "abca" return true // delete c


## 415. Valid Palindrome
https://www.lintcode.com/problem/valid-palindrome

### Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

### Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

### Challenge
O(n) time without extra memory.


## 56. Two Sum
https://www.lintcode.com/problem/two-sum

### Description
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

You may assume that each input would have exactly one solution

### Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

### Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
