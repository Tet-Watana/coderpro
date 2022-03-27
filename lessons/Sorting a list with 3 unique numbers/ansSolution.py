# -*- coding: utf-8 -*-
#多分今回は、回帰とループ処理が組み合わさっているから複雑。
class Solution(object):
    def _permuteHelper(self, nums, start=0):
        #もし、startがnumsの最後だったら、これ以上探索できないのでnumsを返す。
        #ここで戻るのは、result変数のところに戻る。
        if start == len(nums) - 1:  # startは0~1つ手前まで。iは0~最後まで。これで十分swapできる。
            return [nums[:]]  # ←これは小さなループを回すためのもの。回帰用。
        #もし、そうでなかったら、
        result = []
        for i in range(start, len(nums)):
            #numsの中の要素をswapする
            #0番目と0番目をswap→swapした配列をhelperに渡す。startは一つ増やす
            #だから次のループでは、i=start=1になる。
            #その次のループは、start=2になる。つまり、start == len(nums) - 1。
            #print('start, i: ',start, i)
            nums[start], nums[i] = nums[i], nums[start]
            #戻り値は、result変数に格納される。この時点で回帰は終わり。次の行に行ける。
            # start + 1によって、次の階層での注目indexを1つずらすことができる。
            result += self._permuteHelper(nums, start + 1)
            #入れ替えた要素を再swapして元に戻す。元のnumsに戻る。
            nums[start], nums[i] = nums[i], nums[start]
        #ループに入らずに下のreturn resultした場合、前のループまでのhelper出力(result)がreturnされる。それが0,0のときのhelper関数の最終的なresult
        return result  # ←これは一番大きなループを回すためのもの。一番外側のループでは、常にstart=0。iだけが次の値に行く。

    def permute(self, nums):
        #Helper関数を使うことで、numsを傷つけないようにする。
        return self._permuteHelper(nums)  # 一番最後はここに戻ってくる。

    def permute2(self, nums, values=[]):
        if not nums:
            return [values]
        result = []
        for i in range(len(nums)):
            #注目indexの値をnumsから除外する。注目indexの値を、valuesに追加する。
            #iによって、注目indexを徐々にずらしていく。
            #階層が下がると、i=0のままでも、注目indexの値は、自動的にずれていく。
            #nums=[たくさん], val=[]から、最終的にnums=[], val=[たくさん]になるように回帰アルゴリズムができている。
            #nums=[]のときが終了条件であることが、すぐに予想できる。終了のとき、これまでの作ったlistを返す。resultにappendする。
            #smartすぎる。
            result += self.permute2(nums[:i] + nums[i+1:], values + [nums[i]])
        return result


#print(Solution().permute([1, 2, 3]))
#('Final result: ', [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]])

print(Solution().permute2([1, 2, 3]))
