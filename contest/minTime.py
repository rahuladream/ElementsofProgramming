import collections
class Solution:
    def minTime(self, n, edges, hasApple):
        seen = set()
        graph = collections.defaultdict(list)
        def structure(node, parent):
            seen.add(node)
            result = 0
            for val in graph[node]:
                result += structure(val, node)
            
            if hasApple[node] and node != 0:
                hasApple[parent] = True
                return result + 2
            return result
        for u,v in edges:
            graph[u].append(v)        
        return structure(0, 0)


if __name__ == "__main__":
    a = Solution()
    print(a.minTime(7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],[False,False,True,False,True,True,False]))
        