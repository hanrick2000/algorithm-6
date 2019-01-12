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

    
