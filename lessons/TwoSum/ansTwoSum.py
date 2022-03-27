# -*- coding: utf-8 -*-

class Solution(object):
    #brute force solution
    def twoSum(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                # i1,i2の大小関係については制約つけていないからちょっと無駄があるけど、大した無駄ではない。
                if a == b:
                    continue
                #print(i1,i2)
                if a + b == target:
                    return [i1, i2]
        return []

    #clever solution
    #これまで見た値を普通の辞書{}に格納して行く→ in を使うことで、辞書の中を検索する。
    #for文1回だから、TimeComplexityを節約できる。
    def twoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            print(values)
            diff = target - num
            if diff in values:  # 賢い。inを使うことで、検索してる。検索してるのは、keyの部分。
                return[i, values[diff]]
            #keyは値、itemはindex
            values[num] = i
        return []


print(Solution().twoSumB([2, 7, 11, 15], 26))
