class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda K: K[0]**2 + K[1]**2) 
        return points[:K] 


if __name__ == "__main__":
    a = Solution()
    print(a.kClosest(points = [[1,3],[-2,2]], K = 1))