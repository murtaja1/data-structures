class Graph:
    # keys are the vertices.
    # lists contain the edges.
    def __init__(self, graph={}) -> None:
        self.graph=graph
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

cDict = {'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'e'],
        'd': ['b', 'e', 'f'],
        'e': ['d', 'f'],
        'f': ['d','e']}
graph = Graph(cDict)
graph.addEdge('e','c')
print(graph.graph['e'])
        