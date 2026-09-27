# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [0, 1, 2, 3]

         0 -> 1 -> 2 -> 3
         0 <- 1 <- 2 <- 3 

        None <- 0 <- 1 <- 2 -> 3
                          p    t. n

        make a dummy node (prev = None)
        first set dummy's next to the head
        then create two variables at the head

        next will go to the next place
        set temp.next to prev
        move prev to temp
        move temp to next
        
        
        None <-  0 <- 1 <- 2  3
                           p  t    a
        '''

        prev = None
        temp = head

        while temp:
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after
        
        return prev



        