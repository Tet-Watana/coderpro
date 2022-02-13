# -*- coding: utf-8 -*-

#(object)はあってもなくても動作は変わらない。
#Node()の()の中で指定した値は全部initの方の変数に入るから。
#class名のあとには(object)と書くのが一般的らしい。in Techlead
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def _isValidBSTHelper(self, n, low, high): #左側にlow, 右側にhighを置いているのもcodeを見やすくするための工夫。
        if not n: #nが空っぽのとき
            return True
        #nが空っぽでないとき、今のnodeの値を取り出す。
        val = n.val
        #今のnodeの値が、下限~上限の間にあるかチェックする。
        if ((val > low and val < high) and 
            #左下のnode(小)と今のnode(大)との比較する。
            #n.left < n.valかどうかチェックする。最初の条件分岐式で。
            #再帰文だから、左下端までずっとチェックし続ける。このときやっていることは、関数(4,-inf,5)を計算しているだけだから、元のnには影響されない。
            #一番左下端まで行ったら if not n:→Trueが返される。次の処理right側の比較する。何もなかったら、if not n:→Trueが返される。return Trueになる。
            #二番目に左端のnodeに行く。左下側はTrue出てるから、右下側をチェックする。何もなかったら、if not n:→Trueが返される。return Trueになる。
            #これを繰り返して一番上のnodeまで戻ってくる。
            #andでつないでいるので、全部Trueのときのみ、最終判定Trueになる。
            #賢すぎてやばい。
            self._isValidBSTHelper(n.left, low, n.val) and
            self._isValidBSTHelper(n.right, n.val, high)): #右下のnode(大)と今のnode(小)との比較する。n.right > n.valかどうかチェックする。上に同じ。
            return True
        return False

    def isValidBST(self, n): #一番上のnodeを入力する。最初の上限下限は -∞ ~ +∞
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))
        return False

#   5
# /   \
#4      7
node=Node(5) #valに5を代入した
#値5を持ったNodeの中の(に繋がっている)値はこうやって取り出すことができる。値を代入することもできる。
#なんてsmartな書き方
#print(node.val)
#print(node.left)
#print(node.right)
#nodeの左側には別のNodeが繋がっているので、Node(4)を代入する。すごい
node.left=Node(4)
node.right=Node(7)
print(Solution().isValidBST(node))
# True

#    5
#  /   \
# 4     7
#     /
#    2
node=Node(5)
node.left=Node(4)
node.right=Node(7)
node.right.left=Node(2)
print(Solution().isValidBST(node))
#False

#nodeを設計して、nodeの枝のところに別のnodeをつなげるのがsmartだと思った。一番上のnodeを見れば、芋づる式に繋がっているnodeは全部取り出せる。
#自分のclassの中で、自分のclassを呼び出しているのがすごいsmart code.
