# Topological Sort: sorts givin actions in such a way that if there is a 
                # dependency of one action on another, then the dependent action always comes later than its parent. 
                # check visualization\sort\topologicalSort.png /topologicalSortalgorithm.png
from collections import defaultdict

class Graph:
    def __init__(self, numOfVertices) -> None:
        self.numOfVertices = numOfVertices
        self.graph = defaultdict(list)

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    # time complexity is O(V+E)
    # space complexity is O(V+E)
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            # check if any vertex dependent on the current vertex.
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        # if there is no vertex dependent on the current vertex, then add it to the stack.        
        stack.insert(0, vertex)

    def topologicalSort(self):
        stack = []
        visited = []

        for v in list(self.graph):
            if v not in visited:
                self.topologicalSortUtil(v, visited, stack)
        print(stack)


graph = Graph(8)
graph.addEdge("A", "C")
graph.addEdge("C", "E")
graph.addEdge("E", "H")
graph.addEdge("E", "F")
graph.addEdge("F", "G")
graph.addEdge("B", "D")
graph.addEdge("B", "C")
graph.addEdge("D", "F")

print(graph.graph)
graph.topologicalSort()