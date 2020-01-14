# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(None)
        dummyHead = dummy
        while l1 or l2:
            if l1 and l2:
                dummyHead.next = ListNode(l1.val + l2.val)
                dummyHead = dummyHead.next
                l1 = l1.next
                l2 = l2.next
            if l1 and not l2:
                dummyHead.next = ListNode(l1.val)
                dummyHead = dummyHead.next
                l1 = l1.next
            if not l1 and l2:
                dummyHead.next = ListNode(l2.val)
                dummyHead = dummyHead.next
                l2 = l2.next

        dummyHead = dummy.next
        while dummyHead:
            if dummyHead.val >= 10:
                dummyHead.val -= 10
                if dummyHead.next:
                    dummyHead.next.val += 1
                else:
                    dummyHead.next = ListNode(1)
            dummyHead = dummyHead.next
        return dummy.next
