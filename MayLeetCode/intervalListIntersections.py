class Solution:
    def intervalIntersection(self, A, B):
        combined = sorted(A + B, key=itemgetter(0))
        intersection = []
        currentEnd = -1

        for start, end in combined:
            if start <= currentEnd:
                intersection.append([start, min(currentEnd, end)])
            currentEnd = max(currentEnd, end)
        
        return intersection



if __name__ == "__main__":
    a = Solution()
    print(a.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
        