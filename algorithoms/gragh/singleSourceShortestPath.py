# Single Source Shortest Path: finding a path between a givin vertex (Source) to all other vertices in a graph 
                            # such that the total distance between them (source to destination) is minimum. check visualization\graph\singleSourceShortestPath.png 

# Algorithms used to solve SSSP.

    # 1. BFS: check visualization\graph\SSSPBFS.png.

# time complexity is O(E) because we may not visit all the vertices
# space complexity is O(E) because we may not visit all the vertices
class Graph:
    def __init__(self, graph={}) -> None:
        self.graph = graph
    
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path 
            for adjacent in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

cDict = {'a': ['b', 'c'],
        'b': ['a', 'g'],
        'c': ['d', 'e'],
        'd': ['f'],
        'e': ['f'],
        'g': ['f']}
graph = Graph(cDict)
print(graph.bfs('a', 'f'))