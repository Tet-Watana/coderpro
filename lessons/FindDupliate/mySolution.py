# -*- coding: utf-8 -*-
from collections import defaultdict

class Solutions(object):
    def find_non_duplicate(self, val_list):
        d = defaultdict(int)
        for val in val_list:
            d[val] += 1
        for k, v in d.items():
            if v == 1:
                print(k)


val_list = [2, 3, 4, 5, 2, 3, 4]
Solutions().find_non_duplicate(val_list)
# Time Complexity: O(2n) = O(n)
# Space Complexity: O(n)