class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)

    def dfs_iterative(self, start_node):
        stack = [start_node]
        visited = set()

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                print(current_node, end=" ")
                visited.add(current_node)

                for neighbor in self.adj_list[current_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

# Create a graph instance
g = Graph(8)

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

# Perform DFS starting from node 0
g.dfs_iterative(0)
