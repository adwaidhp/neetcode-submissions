class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow1, fast =0 ,0 
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1==fast:
                break
        slow2=0
        while True:
            slow2=nums[slow2]
            slow1=nums[slow1]
            if slow1==slow2:
                break
        return slow1
"""
Based on Floyd's algorithm of cycle detection
[1,3,4,2,2]
Consider it as a linked list
elt at 0th position is 1, in 1 it points to 3rd position, which points to 2nd position, where 4 means it points to the 4th position, where again 2 means that there is a cycle.

Apply Floyd’s Algorithm to find the beginning of a cycle

Floyd’s Algorithm: 
1) Start a slow pointer and a fast pointer which moves twice as fast as the slow pointer. 
2) Move both pointers until the meet at an intersection point. Fix slow pointer at that intersection Point. let that pointer be s1.
3) Start a new slow pointer s2 that moves from the start of the list one step at a time, at the same time move s1 one step at a time. Where s1 and s2 pointers meet, that is going to be the return value (or point of intersection).
"""