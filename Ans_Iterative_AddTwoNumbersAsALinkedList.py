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
        return self.addTwoNumbersIterative(l1, l2)

    def addTwoNumbersIterative(self, l1, l2):
        a = l1  # Node
        b = l2  # Node
        c = 0
        ret = current = None  # retもcurrentもNone

        # while文使ってるからiterativeってことらしい。
        while a or b:  # 少なくとも片方がTrueのとき
            val = a.val + b.val + c  # 最大19
            c = val // 10  # 繰り上げ(carryover)。最大1

            #current == NoneのときTrue
            # 1周目(初回)だけTrueになる。
            if not current:
                # 1の位の計算値を入れる。
                ret = current = Node(val % 10) # 7
            # 2周目以降は、currentに値(Node)が入っているので、else側の処理になる。
            else:
                # currentはNodeなので.nextが使える。
                # Nodeの枝(next)に、新規でNodeを作ってつなげてあげる。
                # whileが動いている間は、Nodeの枝(next)に新規Nodeをつなげ続ける。同時にNode値も設定する。
                current.next = Node(val % 10)
                print('current.next.val:',current.next.val)
                current = current.next
            
            # 少なくとも片方のNodeが次の桁を持っているときTrue
            #両方ともNoneのときはFalse
            if a.next or b.next:
                # 片方のNodeが次の桁を持っていないとき、0を設定してあげて、計算できるようにする。
                if not a.next:
                    a.next = Node(0)
                if not b.next:
                    b.next = Node(0)
            # 次の周の計算を実行できるように変数 = 次の変数 を設定してあげる。そうすれば、次の周でその値を使って次の桁の計算ができる。
            a = a.next
            b = b.next
        return ret

# while文1つだから、Linear Time O(n)
# 最終的な出力も1つのリストだから、Linear Space O(n)

# 342のこと
# 逆からたどると342になる。
l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

# 7→0→8
answer = Solution().addTwoNumbers(l1, l2)
while answer:
    print(answer.val)
    answer = answer.next
