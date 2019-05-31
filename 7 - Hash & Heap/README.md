# 7 - Hash & Heap

## Required (10)

### Easy  642. Moving Average from Data Stream
https://www.lintcode.com/problem/moving-average-from-data-stream

#### Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

#### Example
    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1 // return 1.00000
    m.next(10) = (1 + 10) / 2 // return 5.50000
    m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
    m.next(5) = (10 + 3 + 5) / 3 // return 6.00000


### Easy  494. Implement Stack by Two Queues
https://www.lintcode.com/problem/implement-stack-by-two-queues

#### Description
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

#### Example
    push(1)
    pop()
    push(2)
    isEmpty() // return false
    top() // return 2
    pop()
    isEmpty() // return true


### Easy  209. First Unique Character in a String
https://www.lintcode.com/problem/first-unique-character-in-a-string

#### Description
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

#### Example
For "abaccdeff", return 'b'.

#### Challenge
No extra storage is used.


### Medium  657. Insert Delete GetRandom O(1)
https://www.lintcode.com/problem/insert-delete-getrandom-o1

#### Description
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

#### Example
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();


### Medium  612. K Closest Points
https://www.lintcode.com/problem/k-closest-points

#### Description
Given some points and an origin point in two-dimensional space, find k points which are nearest to the origin.
Return these points sorted by distance, if they are same in distance, sorted by the x-axis, and if they are same in the x-axis, sorted by y-axis.

#### Example
    Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
    return [[1,1],[2,5],[4,4]]


### Medium  544. Top k Largest Numbers
https://www.lintcode.com/problem/top-k-largest-numbers

#### Description
Given an integer array, find the top k largest numbers in it.

#### Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].


### Medium  104. Merge K Sorted Lists
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

### Medium  40. Implement Queue by Two Stacks
https://www.lintcode.com/problem/implement-queue-by-two-stacks

#### Description
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

#### Example
    push(1)
    pop()     // return 1
    push(2)
    push(3)
    top()     // return 2
    pop()     // return 2

#### Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.

### Medium  4. Ugly Number II
https://www.lintcode.com/problem/ugly-number-ii

#### Description
Ugly number is a number that only have factors 2, 3 and 5.

Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Note that 1 is typically treated as an ugly number.

#### Example
If n=9, return 10.

#### Challenge
O(n log n) or O(n) time.

### Hard  134. LRU Cache
https://www.lintcode.com/problem/lru-cache

#### Description
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

#### Example
    Input:
    LRUCache(2)
    set(2, 1)
    set(1, 1)
    get(2)
    set(4, 1)
    get(1)
    get(2)
    Output:
    [1,-1,1]


## Optional (12)

### Easy  495. Implement Stack
https://www.lintcode.com/problem/implement-stack

#### Description
Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

#### Example
    push(1)
    pop()
    push(2)
    top()  // return 2
    pop()
    isEmpty() // return true
    push(3)
    isEmpty() // return false


### Easy  128. Hash Function
https://www.lintcode.com/problem/hash-function

#### Description
In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based big integer like follow:

             hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE

here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).

Given a string as a key and the size of hash table, return the hash value of this key.f

#### Clarification
For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.

#### Example
For key="abcd" and size=100, return 78


### Medium  685. First Unique Number in Data Stream
### Medium  613. High Five
### Medium  606. Kth Largest Element II
### Medium  601. Flatten 2D Vector
### Medium  545. Top k Largest Numbers II
### Medium  526. Load Balancer

### Medium  486. Merge K Sorted Arrays
https://www.lintcode.com/problem/merge-k-sorted-arrays

#### Description
Given k sorted integer arrays, merge them into one sorted array.

#### Example
Given 3 sorted arrays:

    [
      [1, 3, 5, 7],
      [2, 4, 6],
      [0, 8, 9, 10, 11]
    ]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

#### Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.


### Medium  130. Heapify
https://www.lintcode.com/problem/heapify

#### Description
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

#### Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.

#### Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

#### Challenge
O(n) time complexity (**use shiftdown**)


### Medium  129. Rehashing
https://www.lintcode.com/problem/rehashing

#### Description
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

#### Example
Given [null, 21->9->null, 14->null, null],

return
[null, 9->null, null, null, null, 21->null, 14->null, null]


### Medium  124. Longest Consecutive Sequence

## Related (9)

### Easy  551. Nested List Weight Sum
https://www.lintcode.com/problem/nested-list-weight-sum

#### Description
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

#### Example
    Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
    Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)


> ### Easy  494. Implement Stack by Two Queues (same question)

### Medium  575. Decode String
### Medium  541. Zigzag Iterator II
### Medium  540. Zigzag Iterator
### Medium  528. Flatten Nested List Iterator
### Medium  471. Top K Frequent Words

### Medium  224. Implement Three Stacks by Single Array
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


### Hard  24. LFU Cache
