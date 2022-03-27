# -*- coding: utf-8 -*-
#Time Complexity: O(n)
#Space Complexity: O(n)
class Solution(object):
    def getRanges(self, values, target):
        index_list=[i for i, val in enumerate(values) if val == target]
        if index_list==[]:
            return []
        return [index_list[0], index_list[-1]]

values = [1, 3, 3, 5, 7, 8, 9, 9, 15]
target = 9

print(Solution().getRanges(values, target))
