# -*- coding: utf-8 -*-
#arrはソートされているので、binarySearchを使える。TimeComplexityはO(log(n))。めっちゃ短い。
class Solution(object):
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr, 0, len(arr) - 1, target, True) #最後のTrueは、firstかlastかを指定するもの。
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]
    # low: low indexのこと
    # Time Complexity: O(log(n)) binary searchだから
    # Space Complexity: O(log(n)) Time Complexityと同じ。stackするする量と計算時間は相関する。
    def binarySearch(self, arr, low, high, target, findFirst):
        if high < low:
            print('hello')
            return -1
        mid = low + (high - low) // 2
        if findFirst:
            if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                return mid #targetに一致している最初のindex
            if target > arr[mid]: #今の位置の値が小さいので、今の位置より右側を探索する。
                return self.binarySearch(arr, mid + 1, high, target, findFirst)
            if target < arr[mid]: #今の位置が大きいので、今の位置より左側を探索する。
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
        else: #これは、elseちゃんと使わないと、mid == 6のときの処理が抜け落ちる。
            #mid == 6のとき(最初or中間, not最大)は、右側を探索する
            if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                return mid
            elif target < arr[mid]: #今の位置が大きいので、今の位置より左側を探索する
                return self.binarySearch(arr, low, mid - 1, target, findFirst)
            else: # target > arr[mid]: #今の位置が小さいので、今の位置より右側を探索する
                return self.binarySearch(arr, mid + 1, high, target, findFirst)

    #Iterativeって言った場合、whileループのことを差すのか。
    def binarySearchIterative(self, arr, low, high, target, findFirst):
        while True:
            if high < low:
                return -1
            mid = low + (high - low) // 2
            if findFirst:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid #targetに一致している最初のindex
                if target > arr[mid]: #今の位置の値が小さいので、今の位置より右側を探索する。
                    low = mid + 1
                else: #今の位置が大きいので、今の位置より左側を探索する。
                    high = mid - 1
            else: #これは、elseちゃんと使わないと、mid == 6のときの処理が抜け落ちる。
                #mid == 6のとき(最初or中間, not最大)は、右側を探索する
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and arr[mid] == target:
                    return mid
                elif target < arr[mid]: #今の位置が大きいので、今の位置より左側を探索する
                    high = mid - 1
                else: # target > arr[mid]: #今の位置が小さいので、今の位置より右側を探索する
                    low = mid + 1



arr = [1, 3, 3, 5, 7, 8, 9, 9, 15]
x = 9
print(Solution().getRange(arr, x))
