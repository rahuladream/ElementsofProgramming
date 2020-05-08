"""
Straight Line
Referencing the java code
"""


class Solution:
    def slope(self, p1, p2):
        if ((p1[0] - p2[0]) == 0):
            return 0
        else:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def checkStraightLine(self, coordinates):
        p1 = coordinates[1]
        p2 = coordinates[0]
        gSlope = self.slope(p1, p2)
        import pdb; pdb.set_trace()

        for i in range(1, len(coordinates)):
            p1 = coordinates[i]
            p2 = coordinates[0]
            slop = self.slope(p1, p2)
            if (gSlope != slop):
                return False
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
        