class Monkey:
    def findMaxTravel(self, arr):
        tpath = 0
        Path = 0
        j = 0
        for i in range(0, len(arr)):
            while j < i:
                dstnc = (len(arr)-i+j) if (len(arr)-i+j) < (i-j) else (i-j) 
                tpath = arr[i] + arr[j] + dstnc
                import pdb; pdb.set_trace()
                Path = tpath if tpath > Path else Path  
                j += 1
        return Path







if __name__ == "__main__":
    
    n = int(input())
    arry = list(map(int, input().split()))
    a = Monkey()
    print(a.findMaxTravel(arry))