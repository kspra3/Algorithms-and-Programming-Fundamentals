# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

# Initialising vertices and edges.
vertices = int(input("Please input the number of vertices: "))
edges = open("testGraph.txt")

# We create the empty adjacency Matrix.
adjMat = vertices * [0]
for i in range(vertices):
    adjMat[i] = vertices * [0]

# We then generate the adjacency Matrix.
for line in edges:
    adjEdge = line.split()  # Splits each line.
    adjMat[int(adjEdge[0])][int(adjEdge[1])] = 1
    adjMat[int(adjEdge[1])][int(adjEdge[0])] = 1

print("The adjacency Matrix representation of the graph is:\n", adjMat)
