class Solution(object):
    def permutation_dumb(self, val_list):
        for i in range(len(val_list)):
            for j in range(len(val_list)):
                for k in range(len(val_list)):
                    if i != j and j != k and j != k and i != k:
                        val_list2 = [val_list[i], val_list[j], val_list[k]]
                        print(val_list2)


val_list = [0, 1, 2]
Solution().permutation(val_list)
