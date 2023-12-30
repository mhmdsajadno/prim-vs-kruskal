import timeit
import os
# Clearing the Screen
os.system('cls')


def prim(graph):
    n = len(graph)
    mst = []  # Minimum Spanning Tree
    selected = [False] * n  # Track selected vertices

    selected[0] = True  # Start with the first vertex as part of MST

    for _ in range(n - 1):
        min_edge = [None, None, float('inf')]  # [from, to, weight]

        # Iterate through vertices in the MST
        for i in range(n):
            if selected[i]:
                # Iterate through vertices outside the MST
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] < min_edge[2]:
                        # If a valid edge with lower weight is found, update min_edge
                        min_edge = [i, j, graph[i][j]]

        # Add the minimum-weight edge to the MST
        mst.append(min_edge)
        # Mark the destination vertex as selected (part of MST)
        selected[min_edge[1]] = True

    return mst
    
class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
def kruskal(graph, num_vertices):
    # Sort edges in ascending order based on their weights
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])

    # Initialize the disjoint-set
    ds = DisjointSet(num_vertices)

    minimum_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

def time():
    # Use timeit for Prim's algorithm
    prim_time = timeit.timeit(lambda: prim(graph), number=100)

# Use timeit for Kruskal's algorithm
    kruskal_time = timeit.timeit(lambda: kruskal(graph, num_vertices), number=100)

    print("Prim's time:", prim_time)
    print("Kruskal's time:", kruskal_time)
    
# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9]
]
num_vertices = len(graph)

prim_out = prim(graph)
kruskal_out = kruskal(graph, num_vertices)

print("Prim: ")
for edge in prim_out:
    print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")
print("Kruskal: ")
for edge in kruskal_out:
    print(f"{edge[0]} - {edge[1]} (Weight: {edge[2]})")

time()
