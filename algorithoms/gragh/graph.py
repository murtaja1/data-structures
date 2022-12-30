 # what is Graph: Graph consists of two vertices (nodes) and a set of edges connecting these vertices. check visualization\graph\graph.png

 # Graph Terminologies:
    # - Vertices (vertex): the nodes of the graph. check visualization\graph\graph.png
    # - Edge: the line that connects the pairs of vertices. check visualization\graph\graph.png 
    # - Unweighted Graph: does not have weights associated with any edge.
    # - Weighted Graph: has weights associated with any edge. check visualization\graph\weightedGraph.png
    # - Undirected Graph: does not have directions associated with any edge.
    # - Directed Graph: has directions associated with any edge. check visualization\graph\directedGraph.png
    # - Cyclic Graph: has at least one loop. check visualization\graph\cyclicGraph.png
    # - Acyclic Graph: has no loop. check visualization\graph\acyclicGraph.png
    # - Tree: it's a special case of directed acyclic graph. check visualization\graph\tree.png

# Graph Types: check visualization\graph\GraphTypes.png
    # 1. Unweighted-Undirected.
    # 2. Unweighted-Directed.
    # 3. Positive-Weighted-Undirected.
    # 4. Positive-Weighted-Directed.
    # 5. Negative-Weighted-Undirected.
    # 6. Negative-Weighted-Directed.

# Graph Representation:
    # Adjacency Matrix: it's a square matrix or a 2D array. And the element of the matrix indicate 
                      # whether pairs or vertices are adjacent or not in the graph. check visualization\graph\adjacencyMatrix.png
    # Adjacency List: it's a collection of unordered list  used to represent a graph. each list describes 
                    # the set of neighbors of vertex in the graph. check visualization\graph\adjacencyList.png
    # which to use: 
    # if a graph is complete or almost complete we should use Adjacency Matrix.
    # if the number of edges are few then we should use Adjacency List. 