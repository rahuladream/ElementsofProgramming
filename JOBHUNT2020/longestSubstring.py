

class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_ = 0
        start = 0

        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)

            seen[s[end]] = end
            max_ = max(max_, end - start+1)
        return max_
        





if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLongestSubstring("abcabcbb"))