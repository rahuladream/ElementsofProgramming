class Solution:
    def countBits(self, num):
        res = [0]
        while (size := len(res)) < num+1:
            for i in range(size):
                if len(res) == num + 1:
                    break
                res.append(res[i]+1)
        return res