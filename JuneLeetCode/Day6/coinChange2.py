class Solution:
    def change(self, amount, coins):
        tab = [0 for k in range(amount+1)]
        # storing the number of solution
        tab[0] = 1
        # base case (if given value is 0)
        for i in range(0, len(coins)):
            # pick all coins one by one and update the
            # update index greater than or equal to the value
            # of the picked coin
            for j in range(coins[i], amount+1):
                tab[j] += tab[j - coins[i]]
        return tab[amount]





if __name__ == "__main__":
    a = Solution()
    print(a.change(amount = 5, coins = [1, 2, 5]))