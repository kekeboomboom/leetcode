class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_203:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head

        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return sentinel.next


if __name__ == '__main__':
    # Solution_203().removeElements()


    # while ListNode(5):
    #     print("hello")

    print(ListNode(5))