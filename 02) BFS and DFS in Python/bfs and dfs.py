#Input a simple dictionary graph directly

raw_input = input("Enter graph dictionary (example: {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}): ")
graph = eval(raw_input)  

start_node = input("Enter starting node: ")
algorithm = input("Choose (BFS / DFS): ").strip().upper()

#Breadth first search (uses queue)

if algorithm == "BFS":
    visited = [start_node]
    queue = [start_node]
    
    while queue:
        current = queue.pop(0)  
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor) 
                
    print(f"BFS Traversal Order: {visited}")

#Depth first search (uses recursion)

elif algorithm == "DFS":
    visited = []

    def run_dfs(node):
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                run_dfs(neighbor)

    run_dfs(start_node)
    print(f"DFS Traversal Order: {visited}")