# -*- coding: utf-8 -*-

#多分これはbrute forceなやり方。
#TimeComplexity: 最大O(n^2)
#SpaceComplexity: ほぼ0, 現在のval1, val2の値しか記憶しないから。
class bruteSolution(object):
    def TwoSum(self, val_list, target):
        for i in range(len(val_list)): #←nestが2重になっている時点でO(n^2)になる。
            for j in range(len(val_list)):
                if j <= i:
                    continue
                #常にjの方が大きい
                else:
                    val1=val_list[i]
                    val2=val_list[j]
                    sum=val1+val2
                    if sum==target:
                        return[i,j]
        return None

val_list=[2,7,11,15]
target=18
#print(bruteSolution().TwoSum(val_list, target))


#これまで見た値をdefaultdictに保存して置いて、次に見た値を、defaultdictから検索して探すことで、TimeComplexityを節約できるってことかな。
from collections import defaultdict
class Solution(object):
    def TwoSum(self, val_list, target):
        val_dict=defaultdict(int)
        for i in range(len(val_list)):
            val1=val_list[i]
            val_dict[val1] = i
            #print(nums)
            print(val_dict[target-val1])
            if val_dict[target-val1]:
                return val_dict[target-val1], i
        return None

val_list=[2,7,11,15]
target=26
print(Solution().TwoSum(val_list, target))
