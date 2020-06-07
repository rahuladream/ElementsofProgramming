class Solution:
    def change(self, amount, coins):
        tab = [0 for k in range(amount+1)]

        tab[0] = 1

        for i in range(0, len(coins)):
            for j in range(coins[i], amount+1):
                tab[j] += tab[j - coins[i]]
        return tab[amount]





if __name__ == "__main__":
    a = Solution()
    print(a.change(amount = 5, coins = [1, 2, 5]))