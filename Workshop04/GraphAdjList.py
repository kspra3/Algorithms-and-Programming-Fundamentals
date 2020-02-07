# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

# Initialising vertices and edges.
vertices = int(input("Please input the number of vertices: "))
edges = open("testGraph.txt")

# We create the empty adjacency list.
adjList = vertices * [0]
for i in range(vertices):
    adjList[i] = []

# We then generate the adjacency list.
for line in edges:
    adjEdge = line.split()  # Splits each line.
    adjList[int(adjEdge[0])].append(int(adjEdge[1]))
    adjList[int(adjEdge[1])].append(int(adjEdge[0]))

edges.close
print("The adjacency list representation of the graph is:\n", adjList)
