# -*- coding: utf-8 -*-
# 普通の辞書でも、keyが存在しない場合のdefault値を指定できる。dict.get(key, default_val)。

class Solution(object):
    def singleNumber(self, nums):
        occurrence = {}
        for n in nums:
            occurrence[n] = occurrence.get(n, 0) + 1 # key, valueの指定。
        
        for key, value in occurrence.items():
            if value == 1:
                return key

    def singleNumber2(self, nums):
        unique = 0
        for n in nums:
            unique ^= n # unique = unique ^ n
        return unique       


print(Solution().singleNumber2([4, 3, 2, 4, 1, 3, 2]))