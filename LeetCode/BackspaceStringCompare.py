"""
NOTES:
1. two string S and T

S = "ab#c", T = "ad#c"
output => true
ab # remove b => ac

ad#c remove d -> ac
both string are same

"""



class Solution:
    def backspaceCompare(self, S: str, T: str):
        
        def clean_word(string):
            c_s = []
            for str in string:
                if str != "#":
                    c_s.append(str)
                else:
                    if c_s:
                        c_s.pop()
            return c_s
        
        return clean_word(S) == clean_word(T)
        

if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare("a##c", "#a#c"))