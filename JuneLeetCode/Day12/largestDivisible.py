class Solution:    
    def largestDivisibleSubset(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
    

if __name__ == "__main__":
    a = Solution()
    print(a.largestDivisibleSubset([1,2,4,8]))