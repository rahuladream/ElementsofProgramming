class Solution:
    def buildArray(self, target, n):
        value,result = [0], []
        for i in target:
            value.append(i)
            if value[-1] - value[-2] == 1:
                result.append("Push")
            else:
                for j in range(value[-1] - value[-2] - 1):
                    result.append("Push")
                    result.append("Pop")
                result.append("Push")
        return result
    
if __name__ == "__main__":
    a = Solution()
    print(a.buildArray([1,2,3], 3))