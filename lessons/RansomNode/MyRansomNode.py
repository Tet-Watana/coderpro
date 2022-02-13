# -*- coding: utf-8 -*-
#9:22まで

#俺がやったやり方は、多分2番目のやり方に近い。
#TechLeadはsetのはなししていたけど、listでやればB2個も格納できる。
#多分3番目のやり方のほうが効率いいんだろう。

class canspell(object):
    def __init__(self,mag,word):
        self.mag=mag
        self.word=word
    def checkspell(self):
        for char in self.word:
            print(self.mag)
            if char in self.mag:
                self.mag.remove(char)
            else:
                return False
        return True





mag=['A','B','B', 'C','D','E','F']
word='BBED'
print(canspell(mag,word).checkspell())