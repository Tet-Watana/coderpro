# -*- coding: utf-8 -*-
from collections import defaultdict
# Hashmap使うやり方。


class Solution(object):
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1  # 今のitemの値に+1する。初期値0
        # lettersのhashmapは完成した。
        # noteから、cを取り出す。
        for c in note:
            if letters[c] <= 0:
                return False # hashmapに在庫がなかったら、note作れないのでfalse
            letters[c] -= 1 # 在庫有る場合は、在庫から1引く
        # noteの全ての文字を処理できたら、そのnoteは作れるのでTrueを返す。
        return True


print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False
