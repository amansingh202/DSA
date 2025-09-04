## Graph code start

# Array of Edges (Directed) [Start, End]
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# print(A)

# Convert Array of Edges -> Adjacency Matrix

M = []

for i in range(n):
    M.append([0]*n)

for u, v in A:
    M[u][v] = 1

    # for undirected grapgh
    # M[v][u] =  1

# print(M)

from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

    #for undirected graph
    # D[v].append(u)

seen = set()

def dfs_recursive(node):
    print(node)

    for neighbour_node in D[node]:
        if neighbour_node not in seen:
            seen.add(neighbour_node)
            dfs_recursive(neighbour_node)


source  = 0
seen.add(source)
dfs_recursive(source)