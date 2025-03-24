from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    min_path = float('inf')

    cities = [i for i in range(n) if i != start]
    for perm in permutations(cities):
        current_pathweight = 0
        k = start
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][start]
        min_path = min(min_path, current_pathweight)

    return min_path

# Example graph
graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

print("Minimum TSP path:", tsp(graph, 0))
