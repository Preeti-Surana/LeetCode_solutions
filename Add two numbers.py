"""Brute force
- Convert linked lists into numbers, add them, and convert the result back into a linked list."""
- code:-
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        place = 1

        while l1:
            num1 += l1.val * place
            place *= 10
            l1 = l1.next

        place = 1

        while l2:
            num2 += l2.val * place
            place *= 10
            l2 = l2.next

        total = num1 + num2

        dummy = ListNode(0)
        curr = dummy

        if total == 0:
            return dummy

        while total:
            curr.next = ListNode(total % 10)
            total //= 10
            curr = curr.next

        return dummy.next

"""Optimized
- Add nodes digit by digit using carry and create the result linked list simultaneously."""
- code :-

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10

            curr.next = ListNode(total % 10)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

"""- Time: O(max(n,m))
- Space: O(max(n,m))

Recursive
- Perform digit addition recursively by passing the carry to the next node"""
