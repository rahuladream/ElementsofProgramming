"""

"""


def dfs(graph, start=0, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(visited)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return graph


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')