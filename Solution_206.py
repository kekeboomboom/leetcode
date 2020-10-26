from ListNode import ListNode


class Solution_206:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        ret = self.reverseList(head.next)

        head.next.next = head

        head.next = None

        return ret


if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    ret = Solution_206().reverseList(head)

    print(ret.val)
    print(ret.next.val)
    print(ret.next.next.val)
