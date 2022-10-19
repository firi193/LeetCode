class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A=head
        B=head
        while(B!=None):
            B=B.next
            if(B==None):
                return A
            A=A.next
            B=B.next
        return A
