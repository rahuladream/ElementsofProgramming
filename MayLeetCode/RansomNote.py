

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for val in set(ransomNote):
            if not ransomNote.count(val) <= magazine.count(val):
                return False
        return True



if __name__ == "__main__":
    a = Solution()
    print(a.canConstruct("a", "b"))