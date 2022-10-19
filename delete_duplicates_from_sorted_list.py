class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(next=head)
        
        slow=dummy
        fast=head
        while fast.next!=None:
            if fast.next and fast.val==fast.next.val:
                while fast.next and fast.val==fast.next.val:
                    fast=fast.next
                slow.next=fast.next
            else:
                slow=slow.next
            fast=fast.next

        return dummy.next
