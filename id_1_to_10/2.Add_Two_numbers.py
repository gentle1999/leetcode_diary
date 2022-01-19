class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode()
        head = ans
        flag = 0
        flag, new_digit = divmod(l1.val + l2.val + flag, 10)
        ans.val = new_digit
        while l1.next or l2.next or flag:
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode()
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode()
            flag, new_digit = divmod(l1.val + l2.val + flag, 10)
            ans.next = ListNode(val=new_digit)
            ans = ans.next
        return head
