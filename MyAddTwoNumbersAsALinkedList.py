# -*- coding: utf-8 -*-

# 342+465=807
# Linked Listするときは逆の順番で足し算するらしい。
# 多分ビデオは465のところが間違っている。
# ビデオ: 4→6→5
# 本当は: 5→6→4

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    def addTwoNumbers(self, l1, l2):
        # Fill this in.
        if l1 == None or l2 == None:
            return True
        l3 = Node(l1.val + l2.val)
        if len(str(l1.next.val + l2.next.val))==2:
            l3.next = Node(str(l1.next.val + l2.next.val)[1])
            l3.next.next = Node(l1.next.next.val + l2.next.next.val + 1)
        elif len(str(l1.next.val + l2.next.val))==1:
            l3.next = Node(l1.next.val + l2.next.val)
            l3.next.next = Node(l1.next.next.val + l2.next.next.val)
        return l3
    """
    def addTwoNumbers(self, l1, l2):
        node1=l1
        node2=l2
        node1=node1.next
        node2=node2.next

        node3=Node(node1.val+node2.val)
        return l3


# 342のこと
# 逆からたどると342になる。
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

#7→0→8
answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print answer.val
    answer = answer.next
