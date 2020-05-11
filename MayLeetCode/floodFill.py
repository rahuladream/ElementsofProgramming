import numpy as np
class Solution:
    """
    Considered cases:
    1. if x and y outside of screen
    2. color present or not
    3. recursively check and update north, south, east, west
    """
    def floodFill(self, image, sr, sc, newColor):
        shape = np.array(image).shape
        # Getting the shape of array 
        def floodFill(image, x, y, prevC, nextC):
            # check if it four directional or not
            if (x < 0 or x >= shape[0] or y < 0 or y >= shape[1] or image[x][y] != prevC or image[x][y] == nextC):
                return
            
            image[x][y] = nextC
            # new color to update
            floodFill(image, x+1, y, prevC, nextC)
            # recursion for north, south, east and west
            floodFill(image, x-1, y, prevC, nextC)
            floodFill(image, x, y+1, prevC, nextC)
            floodFill(image, x, y-1, prevC, nextC)

        prevC = image[sr][sc]
        # getting the previous color
        floodFill(image, sr, sc, prevC, newColor)
        return image

if __name__ == '__main__':
    a = Solution()
    print(a.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))