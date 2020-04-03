"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""
class Solution:
    def singleNumber(self, arr):
        # 36 ms
        res = 2 * sum(set(arr)) - sum(arr)
        return res


if __name__ == "__main__":
    ar = [2, 2, 1]
    aa = Solution()
    print(aa.findSingle(ar))



class Solution:
    # Took 68ms
    def singleNumber(self, arr):
        non_duplicate_list = []
        for i in arr:
            if i not in non_duplicate_list:
                non_duplicate_list.append(i)
            else:
                non_duplicate_list.remove(i)
        return non_duplicate_list.pop()