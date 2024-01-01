# Minimum Spanning Tree Algorithms

This Python script provides implementations of two well-known algorithms for finding the Minimum Spanning Tree (MST) of a connected, undirected graph: Prim's algorithm and Kruskal's algorithm.

## Overview

A Minimum Spanning Tree is a subset of the edges of a connected, undirected graph that connects all the vertices together without any cycles and has the minimum possible total edge weight. This script offers efficient solutions to compute the MST using Prim's and Kruskal's algorithms.

### Prim's Algorithm

Prim's algorithm starts with an arbitrary node and grows the MST by adding the shortest edge that connects a vertex in the MST to a vertex outside the MST. The process continues until all vertices are included in the MST.

### Kruskal's Algorithm

Kruskal's algorithm follows a different approach. It starts with an empty graph and adds edges to the MST in ascending order of their weights, avoiding cycles in the process.

## Usage

To use the script, import it into your project and call either the `prim` or `kruskal` function with the input graph. The graph should be represented as an adjacency matrix, where `graph[i][j]` represents the weight of the edge between vertices `i` and `j`. The output is a list of edges forming the MST.

```python
# Example usage:
graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]
num_vertices = len(graph)

prim_out = prim(graph)
kruskal_out = kruskal(graph, num_vertices)

# Print the results
print("Prim's Algorithm MST: ")
for edge in prim_out:
    print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")

print("\nKruskal's Algorithm MST: ")
for edge in kruskal_out:
    print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
