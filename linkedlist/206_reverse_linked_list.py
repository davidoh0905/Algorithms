## https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(3)
input1.next.next.next = ListNode(4)
input1.next.next.next.next = ListNode(5)

class Solution(object):
    def reverseList(self, head):
        # Base Case
        if head is None or head.next is None:
            return head

        # the "head" remains to be the "head" before the next recursion started with head.next
        # and the relationship between original "head" and "head.next" remains even after the recursion returns
        p = self.reverseList(head.next) # ex) p : 5->4->3
        head.next.next = head # ex) head : 2 -> 3 ... ==> 2-> 3(head.next) ->2(head.next.next)
        head.next = None # ex) head.next : None

        return p

def listTraverse(head):
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res

print(listTraverse(Solution().reverseList(input1)))

input1 = ListNode(1)
input1.next = ListNode(2)
input1.next.next = ListNode(3)
input1.next.next.next = ListNode(4)
input1.next.next.next.next = ListNode(5)

class iterativeSolution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr is not None:
            print("curr : " , curr.val)
            # pointer set
            next = curr.next
            # reverse
            curr.next = prev
            # next pointer
            prev = curr
            curr = next

        return prev


print(listTraverse(iterativeSolution().reverseList(input1)))


