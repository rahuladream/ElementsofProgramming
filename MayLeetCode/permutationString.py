import itertools
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1h=0
        s2h=0
        if len(s2)<len(s1):
            return False
        for i in s1:
            s1h+=hash(i)
        for i in range(len(s1)):
            s2h+=hash(s2[i])
        if s1h==s2h:
            return True
        if len(s2)>len(s1):
            for j in range(len(s1),len(s2)):
                s2h+=hash(s2[j])-hash(s2[j-len(s1)])
                if s1h==s2h:
                    return True
        return False


if __name__ == "__main__":
    a = Solution()
    print(a.checkInclusion("dinitrophenylhydrazine","acetylphenylhydrazine"))