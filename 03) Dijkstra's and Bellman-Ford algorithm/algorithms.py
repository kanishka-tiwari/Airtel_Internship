# Enter data as a dictionary of connections

raw_input = input("Enter graph dictionary (example input: {"A": [["B", 5], ["C", 2]], "B": [["C", 1]], "C": []}): ")
graph = eval(raw_input)  

start_node = input("Enter starting node: ")
algorithm = input("Choose (dijkstra / bellman): ").strip().lower()

#Track Shortest Distances

distances = {}
for node in graph:
    distances[node] = float('inf')
distances[start_node] = 0

#Dijkstra's algorithm (using list)

if algorithm == "dijkstra":
    unvisited = list(graph.keys())
    
    while unvisited:
        current_node = unvisited[0]
        for node in unvisited:
            if distances[node] < distances[current_node]:
                current_node = node
                
        unvisited.remove(current_node)
        
        for edge in graph[current_node]:
            neighbor = edge[0]
            weight = edge[1]
            
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

#Bellman-Ford algorithm (standard loops)

elif algorithm == "bellman":
    for _ in range(len(graph) - 1):
        for current_node in graph:
            for edge in graph[current_node]:
                neighbor = edge[0]
                weight = edge[1]
                
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

print(f"\nFinal Shortest Distances: {distances}")