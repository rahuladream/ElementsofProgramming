class Solution:
    def ways(self, pizza, cn_k):
        pocket = {}
        def pizzCut(pizz1, pizz2, pizz3, pizz4):
            if any(pizza[i][j] == 'A' for i in range(pizz1, pizz2) for j in range(pizz3, pizz4)):
                return True
        
        def structure(pizz1, pizz2, pizz3, pizz4, cn_k):
            if pizz1 >= pizz2 or pizz3 >= pizz4:
                return 0
            if cn_k == 0:
                return 1
            if (pizz1, pizz2, pizz3, pizz4, cn_k) in pocket:
                return pocket[(pizz1,pizz2, pizz3, pizz4, cn_k)]
            
            res = 0

            for i in range(pizz1 + 1, pizz2):
                if pizzCut(pizz1, i, pizz3, pizz4) and pizzCut(i, pizz2, pizz3, pizz4):
                    res += structure(i, pizz2, pizz3, pizz4, cn_k - 1)

            for j in range(pizz3 + 1, pizz4):
                if pizzCut(pizz1, pizz2, pizz3, j) and pizzCut(pizz1, pizz2, j, pizz4):
                    res += structure(pizz1, pizz2, j, pizz4, cn_k - 1)
            
            pocket[(pizz1, pizz2, pizz3, pizz4, cn_k)] = res
            return res

        return structure(0, len(pizza), 0, len(pizza[0]), cn_k -1) % int(10 ** 9 + 7)

if __name__ == "__main__":
    a = Solution()
    print(a.ways(["A..","AAA","..."], 3))