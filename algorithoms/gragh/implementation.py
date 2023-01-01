class Graph:
    # keys are the vertices.
    # lists contain the edges.
    def __init__(self, graph={}) -> None:
        self.graph=graph
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # Breadth first search: it's for traversing graph data structure. It starts at some arbitrary node of graph and explores neighbor nodes (which are at current level) 
                            # first, before moving  to the next level. check visualization\graph\bfs.png
    # time complexity is O(V+E) where V is the vertices (keys of the dict) and E is the Edges (values of the dict (list)).
    # time complexity is O(V) same as above.
    def bfs(self, vertex): 
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0) # pop the first one coz it's used as queue (fifo)
            print(deVertex)
            for adjacentVertex in self.graph[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    # Depth First Search: It's for traversing a graph data structure which starts selecting an arbitrary node 
                        # and explores as far as possible along each edge before backtracking. check visualization\graph\dfs.png and dfs2.png
    # time complexity is O(V+E) where V is the vertices (keys of the dict) and E is the Edges (values of the dict (list)).
    # time complexity is O(V) same as above.
    def dfs(self, vertex): 
        visited = [vertex]
        stack = [vertex]
        while stack:
            deVertex = stack.pop() # pop the last one coz it's used as stack (lifo)
            print(deVertex)
            for adjacentVertex in self.graph[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)
    

cDict = {'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'e'],
        'd': ['b', 'e', 'f'],
        'e': ['d', 'f'],
        'f': ['d','e']}
graph = Graph(cDict)
graph.addEdge('e','c')
graph.dfs('a')
        