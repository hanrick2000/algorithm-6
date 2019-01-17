# 20190110

## 52. Next Permutation
https://www.lintcode.com/problem/next-permutation

### Description
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

The list may contains duplicate integers.

### Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]


## 190. Next Permutation II
https://www.lintcode.com/problem/next-permutation-ii

### Description
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

### Example
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2

3,2,1 → 1,2,3

1,1,5 → 1,5,1

### Challenge
The replacement must be in-place, do not allocate extra memory.


## 15. Permutations
https://www.lintcode.com/problem/permutations

### Description
Given a list of numbers, return all possible permutations.

You can assume that there is no duplicate numbers in the list.

### Example
For nums = [1,2,3], the permutations are:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

### Challenge
Do it without recursion.


## 16. Permutations II
https://www.lintcode.com/problem/permutations-ii

### Description
Given a list of numbers with duplicate number in it. Find all unique permutations.

### Example
For numbers [1,2,2] the unique permutations are:

    [
      [1,2,2],
      [2,1,2],
      [2,2,1]
    ]

### Challenge
Using recursion to do it is acceptable. If you can do it without recursion, that would be great!


## 197. Permutation Index
https://www.lintcode.com/problem/permutation-index

### Description
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which are ordered in lexicographical order. The index begins at 1.

### Example
Given [1,2,4], return 1.


## 495. Implement Stack
https://www.lintcode.com/problem/implement-stack

### Description
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

### Example
    push(1)
    pop()
    push(2)
    top()  // return 2
    pop()
    isEmpty() // return true
    push(3)
    isEmpty() // return false


## 494. Implement Stack by Two Queues
https://www.lintcode.com/problem/implement-stack-by-two-queues

### Description
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

### Example
    push(1)
    pop()
    push(2)
    isEmpty() // return false
    top() // return 2
    pop()
    isEmpty() // return true


## 224. Implement Three Stacks by Single Array
https://www.lintcode.com/problem/implement-three-stacks-by-single-array

### Description
Implement three stacks by single array.

You can assume the three stacks has the same size and big enough, you don't need to care about how to extend it if one of the stack is full.

### Example
    ThreeStacks(5)  // create 3 stacks with size 5 in single array. stack index from 0 to 2
    push(0, 10) // push 10 in the 1st stack.
    push(0, 11)
    push(1, 20) // push 20 in the 2nd stack.
    push(1, 21)
    pop(0) // return 11
    pop(1) // return 21
    peek(1) // return 20
    push(2, 30)  // push 30 in the 3rd stack.
    pop(2) // return 30
    isEmpty(2) // return true
    isEmpty(0) // return false


## 955. Implement Queue by Circular Array
https://www.lintcode.com/problem/implement-queue-by-circular-array

### Description
Implement queue by circulant array. You need to support the following methods:

CircularQueue(n): initialize a circular array with size n to store elements
boolean isFull(): return true if the array is full
boolean isEmpty(): return true if there is no element in the array
void enqueue(element): add an element to the queue
int dequeue(): pop an element from the queue
it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.

### Example
    CircularQueue(5)
    isFull()   => false
    isEmpty() => true
    enqueue(1)
    dequeue()  => 1


## 128. Hash Function
https://www.lintcode.com/problem/hash-function

### Description
In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:

             hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE

here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).

Given a string as a key and the size of hash table, return the hash value of this key.f

### Clarification
For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.

### Example
For key="abcd" and size=100, return 78


## 129. Rehashing
https://www.lintcode.com/problem/rehashing

### Description
The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

size=3, capacity=4

    [null, 21, 14, null]
           ↓    ↓
           9   null
           ↓
          null
The hash function is:

    int hashcode(int key, int capacity) {
        return key % capacity;
    }
here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

    index:   0    1    2    3     4    5    6   7
    hash : [null, 9, null, null, null, 21, 14, null]
Given the original hash table, return the new hash table after rehashing .

For negative integer in hash table, the position can be calculated as follow:

C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
Python: you can directly use -1 % 3, you will get 2 automatically.

### Example
Given [null, 21->9->null, 14->null, null],

return
[null, 9->null, null, null, null, 21->null, 14->null, null]


## 130. Heapify
https://www.lintcode.com/problem/heapify

### Description
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

### Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.

### Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

### Challenge
O(n) time complexity (**use shiftdown**)


## 104. Merge K Sorted Lists
https://www.lintcode.com/problem/merge-k-sorted-lists

### Description
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

### Example
Given lists:

    [
      2->4->null,
      null,
      -1->null
    ],
return -1->2->4->null.


## 41. Maximum Subarray
https://www.lintcode.com/problem/maximum-subarray

### Description
Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

### Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

### Challenge
Can you do it in time complexity O(n)?


## 44. Minimum Subarray
https://www.lintcode.com/problem/minimum-subarray

### Description
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

The subarray should contain one integer at least.

### Example
For [1, -1, -2, 1], return -3.


## 138. Subarray Sum
https://www.lintcode.com/problem/subarray-sum

### Description
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

### Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].


## 65. Median of two Sorted Arrays
https://www.lintcode.com/problem/median-of-two-sorted-arrays

### Description
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

### Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

### Challenge
The overall run time complexity should be O(log (m+n)).


## 30. Insert Interval
https://www.lintcode.com/problem/insert-interval

### Description
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

### Example
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].

Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
