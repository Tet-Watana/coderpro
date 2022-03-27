# -*- coding: utf-8 -*-

# 342+465=807
# Linked Listするときは逆の順番で足し算するらしい。
# 逆向きにすることで、1の位から順番に上がっていけるから、2桁+3桁の計算がやりやすい。
# 多分ビデオは465のところが間違っている。
# ビデオ: 4→6→5
# 本当は: 5→6→4

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 確かにfor文じゃなくてrecursiveの方がcodeが簡潔でエレガントに見える気がする。
class Solution:
    """
    入力: Node2つ
    出力: Node1つ
    """
    def addTwoNumbers(self, l1, l2):
        #recursiveにするためにはHelper関数を作ったほうがやりやすい
        return self.addTwoNumbersHelper(l1, l2, 0) #第三変数はcarryover(繰り上がりがある場合は1が入る)
    def addTwoNumbersHelper(self, l1, l2, c):
        val = l1.val + l2.val + c #この桁での計算。最大19
        c = val // 10 #今回のvalのcarryover(次の桁の計算用)を計算する。最大1.9。
        ret = Node(val % 10) #この桁の値(returnの略かな)。最大９
        # とりあえずここまでで、今の桁の計算は終わった。

        # ここからは次の桁を計算するために、2つのNodeの次の桁を用意する。
        #1つ上の桁に行ったときに、l1,l2のどちらかが値を持っている場合はTrue
        #どちらもNoneのときは、False
        if l1.next != None or l2.next != None:
            #もし片方の桁数が少ない場合は、少ない方の次の桁を0で補間してあげる。→足し算できるようになる。
            if not l1.next:
                l1.next = Node(0)
            if not l2.next:
                l2.next = Node(0)
            # 次の桁の計算用のNodeの準備はできたので、次の桁の計算する。
            # 計算結果は、ret.nextに保存することで、芋づる式につながる。
            ret.next = self.addTwoNumbersHelper(l1.next, l2.next, c)
        # 最終的にreturnするのは芋づるの一番上の所だけでいい。
        return ret

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
    print(answer.val)
    answer = answer.next
