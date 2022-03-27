# -*- coding: utf-8 -*-
class Solution:
    # list内のperson(要素)を背の高い順に並べ直す。
    # personを、indexに従って、新規配列に配置する。
    # 後から配置されるのは、背の低い人。←背の高い人からは見えないから、背の高い人の順番がずれても大丈夫。
    # 超賢い。
    def reconstructQueue(self, input):
        # sort関数のkeyに自作関数(入力:listの1つの要素,出力:スカラー)を入れると、出力値が小さい順に並ぶ。
        # lambdaのxには、listの要素が順番に入力される。出力は-x[0]。例えば-5。list内の要素は、背の高い順に並べられる。
        input.sort(key=lambda x:-x[0])
        print('sorted input: ', input)
        res = []
        for person in input:
            # person[1]の(index)位置に、person(要素)を配置する。
            res.insert(person[1], person)
        return res


input = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(input))
# [[5,0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]