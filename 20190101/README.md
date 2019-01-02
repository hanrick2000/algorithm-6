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


## 521. Remove Duplicate Numbers in Array
https://www.lintcode.com/problem/remove-duplicate-numbers-in-array

### Description
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
You don't need to keep the original order of the integers.

### Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

### Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.


## 604. Window Sum
https://www.lintcode.com/problem/window-sum

### Description
Given an array of n integers, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.
  
### Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
