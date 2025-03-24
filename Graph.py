from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor] and self.is_cyclic_util(neighbor, visited, rec_stack):
                return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    def is_cyclic(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

# Example usage
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
print("Graph contains cycle:", g.is_cyclic())
