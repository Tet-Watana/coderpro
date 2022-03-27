# -*- coding: utf-8 -*-

# 多分模範解答では、hashmapを使うのだろう。

class Solution(object):
    #actual_num == answer_numになるindexも教えてあげないと。
    def count_persons(self, index, height, answer_num, array):
        count = 0
        correct_index = answer_num
        for j in range(index):
            front_height = array[j][0]
            if front_height >= height:
                count += 1
                if count == answer_num:
                    correct_index = j
        if count < answer_num:
            additional_count = 0
            for k in range(index + 1, len(array)):
                back_height = array[k][0]
                if back_height >= height:
                    additional_count += 1
                if count + additional_count == answer_num:
                    correct_index = k
        return count, correct_index

    # arrayが正しいかどうかを判定
    # 正しくない場合は、間違っているelementのindexをreturnする。正しいindexは、element[1]に入ってる。
    def array_reconstruction(self, array):
        judge = True
        for i, element in enumerate(array):
            height = element[0]
            answer_num = element[1]
            actual_num, correct_index = self.count_persons(i, height, answer_num, array)
            if answer_num == actual_num:
                continue
            else:
                judge = False
                array[i], array[correct_index] = array[correct_index], array[i]
        return array, judge

    def QueueReconstructionByHeight(self, input_array):
        reconstructed_array, judge = self.array_reconstruction(input_array)
        while(not judge):
            reconstructed_array, judge = self.array_reconstruction(reconstructed_array)
        if judge:
            return reconstructed_array


input_array = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
expected_output = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

output_array = Solution().QueueReconstructionByHeight(input_array)
print(output_array == expected_output)
print(output_array)

Space Complexity: O(n^2)